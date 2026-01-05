import time
from config import *
from entities import tower, unit
from systems.spawn_system import SpawnSystem
from systems.unit_system import UnitSystem
from systems.cleanup_system import CleanupSystem
from systems.tower_system import TowerSystem
import map

class Game:
    #Zentrale Spielsimulation
    def __init__(self):
        self.lane = map.Lane([
            (0, 5),
            (10, 5),
            (15, 8),
            (20, 8)
        ])
        
        self.units = []
        self.towers = []
        
        #Beispiel-Tower
        self.towers.append(tower.Tower(8, 5))
        self.towers.append(tower.Tower(14, 5))
        
        self.player_hp = 20
        
        self.spawn_system = SpawnSystem(self.units, self.lane)
        self.unit_system = UnitSystem(self.units)
        self.cleanup_system = CleanupSystem(self.units, self)
        self.tower_system = TowerSystem(self.towers, self.units)

    def update(self, dt):
        #Units spwanen
        self.spawn_system.update(dt)
        
        #Units und Türme updaten
        self.unit_system.update(dt)
        self.tower_system.update(dt)
            
        #Leaks and Deaths aufräumen
        self.cleanup_system.update()
    
    def debug_print(self):
        print(f"Units: {len(self.units)} | Player HP: {self.player_hp}")
        for i, u in enumerate(self.units):
            print(
                f" Unit {i}: "
                f"pos=({u.x:.1f}, {u.y:.1f}) "
                f"hp={u.hp} "
                f"path_index={u.path_index}"
            )
    
    #def draw():
        #draw map, units and towers on the screen
            
### MAIN LOOP ###
if __name__ == "__main__":
    game = Game()

    print("Wintermaul Lane Prototyp gestartet\n")
    
    while game.player_hp > 0:
        game.update(TICK_RATE)
        game.debug_print()
        print("-" * 40)
        time.sleep(TICK_RATE)
import time
from config import *
from entities import tower, unit
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
        
        self.spawn_timer = 0.0
        self.player_hp = 20
        
    def spawn_unit(self):
        self.units.append(unit.Unit(self.lane))




    def update(self, dt):
        #Units spwanen (alle 2 Sekunden)
        self.spawn_timer += dt
        if self.spawn_timer >= 2.0:
            self.spawn_unit()
            self.spawn_timer = 0.0
            
        #Units und Türme updaten
        for unit in self.units:
            unit.update(dt)

        for tower in self.towers:
            tower.update(dt, self.units)
            
        #Leaks and Deaths aufräumen
        for unit in list(self.units):
            if not unit.alive:
                self.units.remove(unit)
            elif unit.path_index >= len(unit.lane.points):
                self.player_hp -= 1
                self.units.remove(unit)
    
    def debug_print(self):
        print(f"Units: {len(self.units)} | Player HP: {self.player_hp}")
        for i, u in enumerate(self.units):
            print(
                f" Unit {i}: "
                f"pos=({u.x:.1f}, {u.y:.1f}) "
                f"hp={u.hp} "
                f"path_index={u.path_index}"
            )
    
    #def Draw():
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
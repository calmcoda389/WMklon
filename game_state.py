from systems.spawn_system import SpawnSystem
from systems.unit_system import UnitSystem
from systems.cleanup_system import CleanupSystem
from systems.tower_system import TowerSystem
from entities import tower
import game_map

class GameState:
    def __init__(self):
        self.player_hp = 20
        self.units = []
        self.towers = []

        self.lane = game_map.Lane([
            (24, 41),
            (8, 41),
            (8, 65),
            (24, 65),
            (24, 80)
        ])

        self.towers.append(tower.Tower(21, 69))
        self.towers.append(tower.Tower(22, 69))
        self.towers.append(tower.Tower(23, 69))
        self.towers.append(tower.Tower(24, 69))
        self.towers.append(tower.Tower(25, 69))
        self.towers.append(tower.Tower(26, 69))
        self.towers.append(tower.Tower(27, 69))
        
        self.towers.append(tower.Tower(28, 71))
        self.towers.append(tower.Tower(22, 71))
        self.towers.append(tower.Tower(23, 71))
        self.towers.append(tower.Tower(24, 71))
        self.towers.append(tower.Tower(25, 71))
        self.towers.append(tower.Tower(26, 71))
        self.towers.append(tower.Tower(27, 71))
        
        self.towers.append(tower.Tower(21, 73))
        self.towers.append(tower.Tower(22, 73))
        self.towers.append(tower.Tower(23, 73))
        self.towers.append(tower.Tower(24, 73))
        self.towers.append(tower.Tower(25, 73))
        self.towers.append(tower.Tower(26, 73))
        self.towers.append(tower.Tower(27, 73))
        
        self.towers.append(tower.Tower(28, 75))
        self.towers.append(tower.Tower(22, 75))
        self.towers.append(tower.Tower(23, 75))
        self.towers.append(tower.Tower(24, 75))
        self.towers.append(tower.Tower(25, 75))
        self.towers.append(tower.Tower(26, 75))
        self.towers.append(tower.Tower(27, 75))


        self.spawn_system = SpawnSystem(self.units, self.lane)
        self.unit_system = UnitSystem(self.units)
        self.cleanup_system = CleanupSystem(
            self.units,
            on_unit_leak=self.on_unit_leak
        )
        self.tower_system = TowerSystem(self.towers, self.units)

    def on_unit_leak(self):
        self.player_hp -= 1

    def update(self, dt):
        self.spawn_system.update(dt)
        self.unit_system.update(dt)
        self.tower_system.update(dt)
        self.cleanup_system.update()
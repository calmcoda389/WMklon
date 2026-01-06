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
            (2, 20),
            (2, 2),
            (20, 2),
            (20, 10),
            (25, 10)
        ])

        self.towers.append(tower.Tower(3, 3))
        self.towers.append(tower.Tower(19, 3))
        self.towers.append(tower.Tower(21, 9))

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
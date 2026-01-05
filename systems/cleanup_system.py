class CleanupSystem:
    def __init__(self, units, game):
        self.units = units
        self.game = game
        
    def update(self):
        for unit in list(self.units):
            if not unit.alive:
                self.units.remove(unit)
            elif unit.path_index >= len(unit.lane.points):
                self.game.player_hp -= 1
                self.units.remove(unit)
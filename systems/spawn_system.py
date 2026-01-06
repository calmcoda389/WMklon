from entities.unit import Unit

class SpawnSystem:
    def __init__(self, units, lane):
        self.units = units
        self. lane = lane
        self. timer = 0.0
        
    def update(self, dt):
        self.timer += dt
        if self.timer >= 1.25:
            self.units.append(Unit(self.lane))
            self.timer = 0.0
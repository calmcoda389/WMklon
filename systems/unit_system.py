class UnitSystem:
    def __init__(self, units):
        self.units = units
        
    def update(self, dt):
        for unit in self.units:
            unit.update(dt)
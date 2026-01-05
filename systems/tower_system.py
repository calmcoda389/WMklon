class TowerSystem:
    def __init__(self, towers, units):
        self.towers = towers
        self. units = units
        
    def update(self, dt):
        for tower in self.towers:
            tower.update(dt, self.units)
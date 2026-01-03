import math
from entities import unit
from config import *

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.range = TOWER_RANGE
        self.damage = TOWER_DAMAGE
        self.attack_speed = TOWER_ATTACK_SPEED
        self.cooldown = 0.0
        
    def update(self, dt, units):
        self.cooldown -= dt
        if self.cooldown <= 0:
            return
        
        target = self.find_target(units)
        if target:
            target.take_damage(self.damage)
            self.cooldown = 1 / self.attack_speed
                
    def distance(self, unit: unit.Unit):
        return math.hypot(self.x - unit.x, self.y - unit.y)
    
    def find_target(self, units):
        #Ziel = Unit mit größtem Fortschritt in Reichweite
        
        candidates = [
            u for u in units
            if u.alive and self.distance(u) <= self.range
        ]
        
        if not candidates:
            return None
        
        return max(candidates, key=lambda u: u.progress())
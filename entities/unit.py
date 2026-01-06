import math
from config import *
import game_map

class Unit:
    def __init__(self, lane: game_map.Lane):
        self.lane = lane
        self.path_index = 0
        
        self.x, self.y = lane.points[0]
        
        self.hp = 100
        self.max_hp = 100
        
        self.move_speed = UNIT_MOVE_SPEED
        
        self.alive = True
        self._progress = 0.0
    
    def current_target(self):
        #Aktueller Wegpunkt
        if self.path_index >= len(self.lane.points):
            return None
        return self.lane.points[self.path_index]
    
    def progress(self):
        return self._progress

    def update(self, dt):
        #Bewegung entlang der Lane
        if not self.alive:
            return
        
        target = self.current_target()
        if target is None:
            return
        
        tx, ty = target
        dx = tx - self.x
        dy = ty - self.y
        dist = math.hypot(dx, dy)
        
        #Wegpunkt erreicht
        if dist < 0.05:
            self.path_index += 1
            self._progress = self.path_index
            return
        
        vx = dx / dist
        vy = dy / dist
        
        self.x += vx * self.move_speed * dt
        self.y += vy * self.move_speed * dt
        
        
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
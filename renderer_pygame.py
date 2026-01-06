import pygame
import game_map

class PygameRenderer:
    def __init__(self, tile_size=12):
        pygame.init()
        self.tile_size = tile_size
        self.screen = pygame.display.set_mode((576, 960))
        pygame.display.set_caption("Wintermaul TD")

    def draw(self, state):
        self.screen.fill((30, 30, 30))

        # Units
        for u in state.units:
            x = int(u.x * self.tile_size)
            y = int(u.y * self.tile_size)
            pygame.draw.circle(self.screen, (200, 50, 50), (x, y), 6)

        # Towers
        for t in state.towers:
            x = int(t.x * self.tile_size)
            y = int(t.y * self.tile_size)
            pygame.draw.rect(
                self.screen,
                (50, 200, 50),
                pygame.Rect(x - 5, y - 5, 10, 10)
            )
        
        # Lane Points (Spawn / Path)
        for px, py in state.lane.points:
            x = int(px * self.tile_size)
            y = int(py * self.tile_size)
            pygame.draw.circle(self.screen, (200, 200, 0), (x, y), 3)
        
        ## Lane Points verbinden
        #points_px = [
        #    (int(px * self.tile_size), int(py * self.tile_size))
        #    for px, py in state.lane.points
        #]

        #if len(points_px) > 1:
        #    pygame.draw.lines(
        #        self.screen,
        #        (80, 80, 220),
        #        False,
        #        points_px,
        #        2
        #    )
        
        pygame.display.flip()
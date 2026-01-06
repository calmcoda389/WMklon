import time
import pygame
from config import TICK_RATE
from game_state import GameState
from renderer_pygame import PygameRenderer

if __name__ == "__main__":
    state = GameState()
    renderer = PygameRenderer()

    clock = pygame.time.Clock()
    running = True

    while running and state.player_hp > 0:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        state.update(dt)
        renderer.draw(state)
    
    pygame.quit()

'''# # # # # # # # # # # # # # # # 
# Headless Test #
print("WintermaulWars Prototyp gestartet\n")

while state.player_hp > 0:
    state.update(TICK_RATE)

    print(f"Units: {len(state.units)} | Player HP: {state.player_hp}")
    for i, u in enumerate(state.units):
        print(
            f" Unit {i}: "
            f"pos=({u.x:.1f}, {u.y:.1f}) "
            f"hp={u.hp} "
            f"path_index={u.path_index}"
        )

    print("-" * 40)
    time.sleep(TICK_RATE)
# # # # # # # # # # # # # # # # # # '''
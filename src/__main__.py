import pygame
import sys
from src.game import Game
from src.art.color import *
from src.const import *
from src.grid.grid import Grid
from src.player.player import Player
from src.const import GameOver
from src.levels import level_0, level_1, level_2
import time
from copy import deepcopy


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Rectangle")

game_over_banner = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
game_over_banner.fill((0, 0, 0, 192))

# Set up the game
cur_level = level_2
game = Game.from_player_and_grid(player=cur_level.player, grid=cur_level.grid)

# Game loop
while True:
    try:
        game.handle_event()
    except GameOver as e:
        screen.blit(game_over_banner, (0, 0))
        pygame.display.flip()
        font = pygame.font.Font(None, 50)
        text1 = font.render(f"GAME OVER! {e}", True, WHITE)
        text2 = font.render(f"Press R to restart", True, WHITE)
        text3 = font.render(f"Press Q to quit", True, WHITE)
        for row, text in enumerate((text1, text2, text3)):
            screen.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    (HEIGHT // 2 - text.get_height() // 2)
                    + text.get_height() * row * 1.5,
                ),
            )
        pygame.display.flip()
        dont_reset = True
        while dont_reset:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_q
                ):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    game = Game.from_player_and_grid(
                        player=cur_level.player, grid=cur_level.grid
                    )
                    dont_reset = False

    screen.fill(BLACK)
    game.grid.draw(screen=screen)
    game.player.draw(screen=screen)
    game.draw_movements(screen=screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

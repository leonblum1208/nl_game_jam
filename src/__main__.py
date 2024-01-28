import pygame
import sys
from src.game import Game
from src.art.color import *
from src.const import *
from src.grid.grid import Grid
from src.player.player import Player, GameOver
from src.levels import level_0, level_1, level_2
import time


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Rectangle")


# Set up the player
game = Game(player=level_2.player, grid=level_2.grid)

# Game loop
while True:
    try:
        game.handle_event()
    except GameOver:
        break

    screen.fill(BLACK)
    game.grid.draw(screen=screen)
    game.player.draw(screen=screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

while True:
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Press Q to Quit", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_active = False
                pygame.quit()
                sys.exit()

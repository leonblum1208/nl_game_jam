import pygame
import sys
from src.game import Game, Player
from src.art.color import *
from src.const import *
from src.grid.grid import Grid
import src.levels.level_1 as level_1

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Rectangle")


# Set up the player
game = Game(player=level_1.player, grid=level_1.grid)

# Game loop
while True:
    game.handle_event()

    screen.fill(BLACK)
    game.grid.draw(screen=screen)
    game.player.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

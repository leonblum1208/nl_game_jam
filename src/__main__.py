import pygame
import sys
from src.game import Game, Player
from src.art.color import *
from src.const import *
from src.grid.grid import Grid
from src.levels import level_1, level_2
import time


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Rectangle")


# Set up the player
game = Game(player=level_2.player, grid=level_2.grid)

# Game loop
while True:
    if game.player.num_movements == 1:
        game.grid.update(turns=1)
        game.player.num_movements = 0
    game.handle_event()
    screen.fill(BLACK)
    game.grid.draw(screen=screen)
    game.player.draw(screen)

    pygame.display.flip()


    pygame.time.Clock().tick(10)

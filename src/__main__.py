import pygame
import sys
from src.game import Game, Player
from src.art.color import *
from src.const import *
from src.grid.grid import Grid
from src.levels.level_1 import LEVEL_1
from src.art.image import Image

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Rectangle")


# Set up the player
image = Image(image_name="Right.png")
player_col_start, player_row_start = 0, 0
player = Player(col=player_col_start, row=player_row_start, image=image)
game = Game(player=player, grid=LEVEL_1)

# Game loop
while True:
    game.handle_event()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw player
    game.grid.draw(screen=screen)
    game.player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

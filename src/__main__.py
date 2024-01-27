import pygame
import sys
from src.game import Game, Player
from src.art.color import *
from src.const import *
from src.grid.grid import Grid
from src.levels.level_1 import LEVEL_1

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Rectangle")


# Set up the player
player_col_start, player_row_start = 0, 0
player = Player(width=25, height=20, col=player_col_start, row=player_row_start)
game = Game(player=player, grid=LEVEL_1)

# Game loop
while True:
    game.handle_event()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw player
    game.player.draw(screen, WHITE, PIX_PER_TILE)
    game.grid.draw(screen=screen)
    
    pygame.draw.rect(
        screen,
        (255,0,0, 128),
        (0,0,50,50),
    )

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

import pygame
import sys
from src.game import Game, Player

# Initialize Pygame
pygame.init()

# Parameters
TILE_SIZE = 50

# Set up display
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movable Rectangle")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the player
player_col_start, player_row_start = 0, 0
player = Player(width=25, height=20, col=player_col_start, row=player_row_start)
game = Game(player=player)

# Game loop
while True:
    game.handle_event()

    # Fill the screen with black
    screen.fill(black)

    #Draw player
    player.draw(screen, white, TILE_SIZE)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

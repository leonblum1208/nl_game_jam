import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movable Rectangle")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the rectangle
rect_width, rect_height = 50, 50
rect_x, rect_y = (width - rect_width) // 2, (height - rect_height) // 2
rect_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT] and rect_x < width - rect_width:
        rect_x += rect_speed
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN] and rect_y < height - rect_height:
        rect_y += rect_speed

    # Fill the screen with black
    screen.fill(black)

    # Draw the rectangle
    pygame.draw.rect(screen, white, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

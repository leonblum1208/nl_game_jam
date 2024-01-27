import pygame
from pydantic import BaseModel
from src.const import *

class Arrow(BaseModel):
    length: int = PIX_PER_TILE/2.5
    head_size: int = PIX_PER_TILE/8
    color: tuple
    direction: str #['up', 'down', 'left', 'right']

    def draw(self, screen, pos_x, pos_y):
        direction_map = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }
        dx, dy = direction_map.get(self.direction, (0,0))
        # Draw arrow shaft (line)
        pygame.draw.line(screen, self.color, (pos_x, pos_y), (pos_x + dx * (self.length - self.head_size), pos_y + dy * (self.length - self.head_size)), 2)
        # Draw arrowhead (triangle)
        arrowhead = [
            (pos_x + dx * self.length, pos_y + dy * self.length),
            (pos_x + dx * (self.length - self.head_size) - dy * self.head_size, pos_y + dy * (self.length - self.head_size) + dx * self.head_size),
            (pos_x + dx * (self.length - self.head_size) + dy * self.head_size, pos_y + dy * (self.length - self.head_size) - dx * self.head_size)
        ]
        pygame.draw.polygon(screen, self.color, arrowhead)
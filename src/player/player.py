import pygame
from pydantic import BaseModel

class Player(BaseModel):
    width:int
    height: int
    col: int
    row: int

    def move(self, dcol, drow):
        self.col += dcol
        self.row += drow

    def draw(self, screen, white, TILE_SIZE):
        pos_x = self.col * TILE_SIZE + (TILE_SIZE - self.width)/2
        pos_y = self.row * TILE_SIZE + (TILE_SIZE - self.height) / 2
        pygame.draw.rect(screen, white, (pos_x, pos_y, self.width, self.height))
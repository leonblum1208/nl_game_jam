import pygame
from pydantic import BaseModel
from src.art.arrow import Arrow
from src.art.image import Image
from src.art.color import *
from src.const import *
from pathlib import Path


class Player(BaseModel):
    size: int = 0.9
    col: int
    row: int
    image: Image

    def move(self, dcol, drow):
        self.col += dcol
        self.row += drow

    def draw(self, screen):
        image_surface = self.image.load()
        image_rect = image_surface.get_rect()
        scaled_image_surface = self.image.scale(image_surface, image_rect, self.size)
        scaled_image_rect = scaled_image_surface.get_rect(
            topleft=(self.col * TILE_WIDTH_PIX, self.row * TILE_HEIGHT_PIX)
        )
        screen.blit(scaled_image_surface, scaled_image_rect)
        # pos_x = self.col * TILE_WIDTH_PIX + (TILE_WIDTH_PIX - self.width)/2
        # pos_y = self.row * TILE_HEIGHT_PIX + (TILE_HEIGHT_PIX - self.height) / 2
        # pygame.draw.rect(screen, color, (pos_x, pos_y, self.width, self.height))
        # self.arrow.draw(screen,pos_x, pos_y)

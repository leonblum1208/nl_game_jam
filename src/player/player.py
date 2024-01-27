import pygame
from pydantic import BaseModel
from enum import Enum
from src.art.arrow import Arrow
from src.art.image import Image
from src.art.color import *
from src.const import *
from pathlib import Path

class PlayerDirection(int, Enum):
    UP: int = 0
    RIGHT: int = 1
    DOWN: int = 2
    LEFT: int = 3

class Player(BaseModel):
    size: int = 0.6
    col: int
    row: int
    face_direction: PlayerDirection
    num_movements: int = 0

    @property
    def image(self) -> Image:
        return Image(image_name = f"Robo-{self.face_direction.name}.png")

    def turn(self, direction_change):
        self.face_direction = PlayerDirection((self.face_direction.value + direction_change) % 4)
        print(self.face_direction.value)
        self.num_movements += 1

    def move(self, step):
        if self.face_direction == PlayerDirection.RIGHT:
            self.col += step
        elif self.face_direction == PlayerDirection.LEFT:
            self.col -= step
        elif self.face_direction == PlayerDirection.DOWN:
            self.row += step
        elif self.face_direction == PlayerDirection.UP:
            self.row -= step
        self.num_movements += 1

    def draw(self, screen):
        image_surface = self.image.load()
        image_rect = image_surface.get_rect()
        scaled_image_surface = self.image.scale(image_surface, image_rect, self.size)
        scaled_image_rect = scaled_image_surface.get_rect()
        scaled_image_rect.topleft = (self.col * TILE_WIDTH_PIX + (TILE_WIDTH_PIX - scaled_image_rect.width)/2, self.row * TILE_HEIGHT_PIX + (TILE_HEIGHT_PIX - scaled_image_rect.height) / 2)
        screen.blit(scaled_image_surface, scaled_image_rect)
        # pos_x = self.col * TILE_WIDTH_PIX + (TILE_WIDTH_PIX - self.width)/2
        # pos_y = self.row * TILE_HEIGHT_PIX + (TILE_HEIGHT_PIX - self.height) / 2
        # pygame.draw.rect(screen, color, (pos_x, pos_y, self.width, self.height))
        # self.arrow.draw(screen,pos_x, pos_y)

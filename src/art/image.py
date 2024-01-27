import pygame
from pydantic import BaseModel
from pathlib import Path
from src.const import *

graphics_folder = Path(__file__).parent / "graphics"


class Image(BaseModel):
    image_name: str = "RIGHT.png"  # ["RIGHT.png", "LEFT.png", "UP.png", "DOWN.png"]

    def load(self):
        image_path = graphics_folder / self.image_name
        image_surface = pygame.image.load(image_path)
        return image_surface

    def scale(self, image_surface, image_rect, size):
        scale_factor_width = TILE_WIDTH_PIX / image_rect.width
        scale_factor_height = TILE_HEIGHT_PIX / image_rect.height
        scale_factor = min(scale_factor_width, scale_factor_height) * size
        scaled_image = pygame.transform.scale(
            image_surface,
            (
                int(image_rect.width * scale_factor),
                int(image_rect.height * scale_factor),
            ),
        )
        return scaled_image

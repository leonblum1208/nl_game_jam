import pygame
from pydantic import BaseModel
from pathlib import Path
from src.const import *

graphics_folder = Path(__file__).parent / "graphics"



class Image(BaseModel):
    surface: pygame.Surface
    rect: pygame.Rect
    model_config = {"arbitrary_types_allowed":True}

    @classmethod
    def from_path(cls, image_name: str):
        image_path = graphics_folder / image_name
        image_surface = pygame.image.load(image_path)
        image_rect = image_surface.get_rect()
        return cls(surface=image_surface, rect=image_rect)

    def scale(self, size):
        scale_factor_width = TILE_WIDTH_PIX / self.rect.width
        scale_factor_height = TILE_HEIGHT_PIX / self.rect.height
        scale_factor = min(scale_factor_width, scale_factor_height) * size
        scaled_image = pygame.transform.scale(
            self.surface,
            (
                int(self.rect.width * scale_factor),
                int(self.rect.height * scale_factor),
            ),
        )
        return scaled_image

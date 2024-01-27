import pygame
from typing import Optional, Tuple
from pydantic import BaseModel
from enum import Enum
from src.art.color import *
from src.const import *
from src.art.image import Image


class TilePosition(BaseModel):
    row: int
    col: int

    @property
    def x0(self) -> int:
        return self.col * TILE_WIDTH_PIX

    @property
    def y0(self) -> int:
        return self.row * TILE_HEIGHT_PIX

    def x0_plus_gap(self, rel_width: float) -> int:
        return self.x0 + ((1 - rel_width) * TILE_WIDTH_PIX) / 2

    def y0_plus_gap(self,  rel_height: float) -> int:
        return self.y0 + ((1 - rel_height) * TILE_HEIGHT_PIX) / 2

    def get_rect(
        self, rel_width: float, rel_height: float
    ) -> Tuple[int, int, int, int]:
        return (
            self.x0_plus_gap(rel_width),
            self.y0_plus_gap(rel_height),
            TILE_WIDTH_PIX * rel_width,
            TILE_HEIGHT_PIX * rel_height,
        )


class TileData(BaseModel):
    color: Optional[tuple] = None
    rel_width: float = 0.99
    rel_height: float = 0.99
    model_config = {"arbitrary_types_allowed": True}


class BaseTileData(TileData):
    rel_width: float = 0.99
    rel_height: float = 0.99


class AddOnData(TileData):
    rel_width: float = 0.5
    rel_height: float = 0.5


class BaseTile(Enum):
    EMPTY: BaseTileData = BaseTileData(color=BLACK)
    CONVEYER: BaseTileData = BaseTileData(color=GREY)
    START: BaseTileData = BaseTileData(color=ORANGE)
    END: BaseTileData = BaseTileData(color=GREEN)
    PLATFORM: BaseTileData = BaseTileData(color=DARK_GREY)


class AddOn(Enum):
    NONE: AddOnData = AddOnData()
    CHEST: AddOnData = AddOnData(color=BROWN)
    HOLE: AddOnData = AddOnData(color=VERY_DARK_GREY)
    LEFT_TURN: AddOnData = AddOnData(color=WHITE)
    RIGHT_TURN: AddOnData = AddOnData(color=WHITE)


class Tile(BaseModel):
    base: BaseTileData = BaseTile.EMPTY
    add_on: AddOnData = AddOn.NONE

    def draw(self, screen: pygame.Surface, pos: TilePosition, image: Optional[Image] = None) -> None:
        if image:
            scaled_image_surface = image.scale(size=min(self.base.rel_height, self.base.rel_width))
            scaled_image_rect = scaled_image_surface.get_rect()
            scaled_image_rect.topleft = (pos.x0_plus_gap(rel_width=self.base.rel_width), pos.y0_plus_gap(rel_height=self.base.rel_height))
            screen.blit(scaled_image_surface, scaled_image_rect)
        elif self.base.color:
            pygame.draw.rect(
                screen,
                self.base.color,
                pos.get_rect(self.base.rel_width, self.base.rel_height),
            )
        if self.add_on.color:
            pygame.draw.rect(
                screen,
                self.add_on.color,
                pos.get_rect(self.add_on.rel_width, self.add_on.rel_height),
            )

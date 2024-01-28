import pygame
from typing import Optional, Tuple
from pydantic import BaseModel
from enum import Enum
from src.art.color import *
from src.const import *
from src.art.image import Image
from src.art.add_ons import ADDON_IMAGES


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
    rel_width: float = 0.8
    rel_height: float = 0.8
    image_name: Optional[str] = None

    @property
    def image(self) -> Optional[Image]:
        return ADDON_IMAGES.get(self.image_name)


class BaseTile(Enum):
    EMPTY: BaseTileData = BaseTileData(color=BLACK)
    CONVEYER: BaseTileData = BaseTileData(color=GREY)
    START: BaseTileData = BaseTileData(color=ORANGE)
    END: BaseTileData = BaseTileData(color=GREEN)
    PLATFORM: BaseTileData = BaseTileData(color=DARK_GREY)


class AddOn(Enum):
    NONE: AddOnData = AddOnData()
    CHEST: AddOnData = AddOnData(color=BROWN, image_name="Kiste")
    HOLE: AddOnData = AddOnData(color=VERY_DARK_GREY, image_name="Hole")
    LEFT_TURN: AddOnData = AddOnData(color=WHITE)
    RIGHT_TURN: AddOnData = AddOnData(color=WHITE)


class Tile(BaseModel):
    base_type:BaseTile
    add_on_type:AddOn
    @property
    def base(self) -> BaseTileData:
        return self.base_type.value
    @property
    def add_on(self) -> AddOnData:
        return self.add_on_type.value

    def draw(self, screen: pygame.Surface, pos: TilePosition, base_image: Optional[Image] = None) -> None:
        if base_image:
            scaled_image_surface = base_image.scale(size=min(self.base.rel_height, self.base.rel_width))
            scaled_image_rect = scaled_image_surface.get_rect()
            scaled_image_rect.topleft = (pos.x0_plus_gap(rel_width=self.base.rel_width), pos.y0_plus_gap(rel_height=self.base.rel_height))
            screen.blit(scaled_image_surface, scaled_image_rect)
        elif self.base.color:
            pygame.draw.rect(
                screen,
                self.base.color,
                pos.get_rect(self.base.rel_width, self.base.rel_height),
            )
        if self.add_on.image:
            scaled_add_on_image_surface = self.add_on.image.scale(size=min(self.add_on.rel_height, self.add_on.rel_width))
            scaled_add_on_image_rect = scaled_add_on_image_surface.get_rect()
            scaled_add_on_image_rect.topleft = (pos.x0_plus_gap(rel_width=self.add_on.rel_width), pos.y0_plus_gap(rel_height=self.add_on.rel_height))
            screen.blit(scaled_add_on_image_surface, scaled_add_on_image_rect)
        elif self.add_on.color:
            pygame.draw.rect(
                screen,
                self.add_on.color,
                pos.get_rect(self.add_on.rel_width, self.add_on.rel_height),
            )

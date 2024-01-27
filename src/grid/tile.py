import pygame
from typing import Optional, Tuple
from pydantic import BaseModel
from enum import Enum
from src.art.color import *
from src.const import *


class TilePosition(BaseModel):
    row: int
    col: int

    @property
    def x0(self) -> int:
        return self.col * TILE_WIDTH_PIX

    @property
    def y0(self) -> int:
        return self.row * TILE_HEIGHT_PIX

    def get_rect(
        self, rel_width: float, rel_height: float
    ) -> Tuple[int, int, int, int]:
        x_gap = ((1 - rel_width) * TILE_WIDTH_PIX) / 2
        y_gap = ((1 - rel_height) * TILE_HEIGHT_PIX) / 2
        return (
            self.x0 + x_gap,
            self.y0 + y_gap,
            TILE_WIDTH_PIX * rel_width,
            TILE_HEIGHT_PIX * rel_height,
        )


class TileData(BaseModel):
    color: Optional[tuple] = None
    rel_width: float = 1
    rel_height: float = 1


class BaseTileData(TileData):
    rel_width: float = 0.9
    rel_height: float = 0.9


class AddOnData(TileData):
    rel_width: float = 0.5
    rel_height: float = 0.5

class BaseTile(Enum):
    EMPTY:BaseTileData = BaseTileData(color=BLACK)
    CONVEYER:BaseTileData = BaseTileData(color=GREY)
    START:BaseTileData = BaseTileData(color=ORANGE)
    END:BaseTileData = BaseTileData(color=GREEN)
    PLATFORM:BaseTileData = BaseTileData(color=DARK_GREY)


class AddOn(Enum):
    NONE:AddOnData = AddOnData()
    CHEST:AddOnData = AddOnData(color=BROWN)
    HOLE:AddOnData = AddOnData(color=VERY_DARK_GREY)
    LEFT_TURN:AddOnData = AddOnData(color=WHITE)
    RIGHT_TURN:AddOnData = AddOnData(color=WHITE)


class Tile(BaseModel):
    base: BaseTileData = BaseTile.EMPTY
    add_on: AddOnData = AddOn.NONE
    pos: TilePosition

    def draw(self, screen: pygame.Surface) -> None:
        if self.base.color:
            pygame.draw.rect(
                screen,
                self.base.color,
                self.pos.get_rect(self.base.rel_width, self.base.rel_height),
            )
        if self.add_on.color:
            pygame.draw.rect(
                screen,
                self.add_on.color,
                self.pos.get_rect(self.add_on.rel_width, self.add_on.rel_height),
            )

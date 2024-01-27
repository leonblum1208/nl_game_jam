from collections import deque
from enum import Enum
from typing import List, Deque
from pydantic import BaseModel
import pygame
from src.grid.tile import AddOn, AddOnData, BaseTileData, Tile, BaseTile, TilePosition


class ConveyerDirection(Enum):
    RIGHT: int = 1
    LEFT: int = -1


class RowDefinition(BaseModel):
    base_tiles: List[BaseTile]
    add_ons: List[AddOn]


class Row(BaseModel):
    tiles: Deque[Tile]

    def update(self, turns: int = 1) -> None:
        _ = turns

    def draw(self, screen: pygame.Surface, row: int) -> None:
        for col, tile in enumerate(self.tiles):
            tile.draw(screen, TilePosition(row=row, col=col))

    @classmethod
    def from_tile_lists(cls, row: int, row_def: RowDefinition) -> "Row":
        tiles = deque()
        for col, (base_tile, add_on) in enumerate(
            zip(row_def.base_tiles, row_def.add_ons)
        ):
            tile = Tile(
                base_type=base_tile,
                add_on_type=add_on,
                pos=TilePosition(row=row, col=col),
            )
            tiles.append(tile)
        return cls(tiles=tiles)


class Conveyer(Row):
    direction: ConveyerDirection = ConveyerDirection.LEFT
    speed: int = 1

    def update(self, turns: int = 1) -> None:
        self.tiles.rotate(self.direction.value * turns)

    @classmethod
    def from_add_on_list(
        cls,
        row: int,
        add_ons: List[AddOn],
        direction: ConveyerDirection = ConveyerDirection.LEFT,
        speed: int = 1,
    ) -> "Conveyer":
        tiles = deque()
        for col, add_on in enumerate(add_ons):
            tile = Tile(
                base_type=BaseTile.CONVEYER,
                add_on_type=add_on,
                pos=TilePosition(row=row, col=col),
            )
            tiles.append(tile)
        return cls(tiles=tiles, direction=direction, speed=speed)

from collections import deque
from typing import List, Deque
from pydantic import BaseModel
import pygame
from src.grid.tile import AddOn, AddOnData, BaseTileData, Tile, BaseTile, TilePosition


class RowDefinition(BaseModel):
    base_tiles: List[BaseTileData]
    add_ons: List[AddOnData]


class Row(BaseModel):
    tiles: Deque[Tile]

    def draw(self, screen: pygame.Surface) -> None:
        for tile in self.tiles:
            tile.draw(screen)

    @classmethod
    def from_tile_lists(cls, row: int, row_def: RowDefinition) -> "Row":
        tiles = deque()
        for col, (base_tile, add_on) in enumerate(
            zip(row_def.base_tiles, row_def.add_ons)
        ):
            tile = Tile(
                base=base_tile,
                add_on=add_on,
                pos=TilePosition(row=row, col=col),
            )
            tiles.append(tile)
        return cls(tiles=tiles)


class Conveyer(Row):
    @classmethod
    def from_add_on_list(cls, row: int, add_ons: List[AddOn]) -> "Conveyer":
        tiles = deque()
        for col, add_on in enumerate(add_ons):
            tile = Tile(
                base=BaseTile.CONVEYER.value,
                add_on=add_on,
                pos=TilePosition(row=row, col=col),
            )
            tiles.append(tile)
        return cls(tiles=tiles)

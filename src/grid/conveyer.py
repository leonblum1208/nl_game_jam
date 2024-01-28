from collections import deque
from enum import Enum
from typing import List, Deque
from pydantic import BaseModel
import pygame
from src.grid.tile import AddOn, AddOnData, BaseTileData, Tile, BaseTile, TilePosition
from src.art.image import Image
from src.art.conveyer_belt import CONVEYER_IMAGES
from src.player.player_info import PlayerDirection


class RowDefinition(BaseModel):
    base_tiles: List[BaseTile]
    add_ons: List[AddOn]


class Row(BaseModel):
    tiles: Deque[Tile]

    @property
    def base_image(self) -> None:
        return None

    def update(self, turns: int = 1) -> None:
        _ = turns

    def draw(self, screen: pygame.Surface, row: int) -> None:
        for col, tile in enumerate(self.tiles):
            tile.draw(
                screen, TilePosition(row=row, col=col), base_image=self.base_image
            )

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
    direction: PlayerDirection = PlayerDirection.LEFT
    speed: int = 1

    @property
    def base_image(self) -> Image:
        return CONVEYER_IMAGES[self.direction]

    def update(self, turns: int = 1) -> None:
        if self.direction in (PlayerDirection.LEFT, PlayerDirection.UP):
            self.tiles.rotate(-1 * turns)
        elif self.direction in (PlayerDirection.RIGHT, PlayerDirection.DOWN):
            self.tiles.rotate(1 * turns)

    @classmethod
    def from_add_on_list(
        cls,
        row: int,
        add_ons: List[AddOn],
        direction: PlayerDirection = PlayerDirection.LEFT,
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

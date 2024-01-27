from collections import deque
from pydantic import BaseModel
import pygame
from typing import Deque

from src.art.color import WHITE
from src.grid.conveyer import Row
from src.grid.tile import Tile
from src.player.player_info import PlayerPosition


class Grid(BaseModel):
    n_rows: int
    n_cols: int
    rows: Deque[Row]

    def draw(self, screen: pygame.Surface) -> None:
        for row, row_obj in enumerate(self.rows):
            row_obj.draw(screen, row=row)

    def update(self, turns: int = 1):
        for row in self.rows:
            row.update(turns=turns)

    def get_tile(self, pos: PlayerPosition) -> Tile:
        return self.rows[pos.row].tiles[pos.col]

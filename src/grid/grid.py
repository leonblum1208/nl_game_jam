from collections import deque
from pydantic import BaseModel
import pygame
from typing import Deque, List

from src.art.color import WHITE
from src.grid.conveyer import Row
from src.grid.tile import Tile
from src.const import GameOver
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

    def get_tile(self, pos: PlayerPosition, game_over_messages: List[str] = []) -> Tile:
        if (
            pos.col < 0
            or pos.row < 0
            or pos.row >= self.n_rows
            or pos.col >= self.n_cols
        ):
            game_over_messages.append("You tried to walk on nothing")
        return self.rows[pos.row].tiles[pos.col]

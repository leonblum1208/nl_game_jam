from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from enum import Enum


class PlayerDirection(int, Enum):
    UP: int = 0
    RIGHT: int = 1
    DOWN: int = 2
    LEFT: int = 3

    @property
    def opposite(self) -> "PlayerDirection":
        if self == PlayerDirection.UP:
            return PlayerDirection.DOWN
        elif self == PlayerDirection.DOWN:
            return PlayerDirection.UP
        elif self == PlayerDirection.RIGHT:
            return PlayerDirection.LEFT
        return PlayerDirection.RIGHT

    @staticmethod
    def get_direction_from_positions(
        start: PlayerPosition, end: PlayerPosition
    ) -> Optional[PlayerDirection]:
        dcol = end.col - start.col
        drow = end.row - start.row
        if dcol > 0:
            return PlayerDirection.RIGHT
        if dcol < 0:
            return PlayerDirection.LEFT
        if drow > 0:
            return PlayerDirection.DOWN
        if drow < 0:
            return PlayerDirection.UP
        return None


class PlayerPosition(BaseModel):
    col: int
    row: int
    face_direction: PlayerDirection

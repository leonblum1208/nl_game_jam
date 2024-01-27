from pydantic import BaseModel
from enum import Enum


class PlayerDirection(int, Enum):
    UP: int = 0
    RIGHT: int = 1
    DOWN: int = 2
    LEFT: int = 3


class PlayerPosition(BaseModel):
    col: int
    row: int
    face_direction: PlayerDirection

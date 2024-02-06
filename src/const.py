from pydantic import BaseModel
from enum import Enum

WIDTH = 1280
HEIGHT = 720
PIX_PER_TILE = 100
TILE_WIDTH_PIX = PIX_PER_TILE
TILE_HEIGHT_PIX = PIX_PER_TILE


class MessageType(Enum):
    SUCCESS: int = 1
    FAIL: int = 0


class GameOverMessage(BaseModel):
    type: MessageType
    message: str


class GameOver(Exception):
    pass

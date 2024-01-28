from collections import deque
from typing import List
from src.grid.grid import Grid
from src.grid.conveyer import Row, Conveyer, RowDefinition, PlayerDirection
from src.grid.tile import *
from src.art.image import Image
from src.game import Player
from src.player.player_info import PlayerDirection, PlayerPosition
from src.player.player import PlayerDirection
from src.player.player_info import PlayerPosition

start_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value] * 4
    + [BaseTile.START.value]
    + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 6,
)
basic_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value]
    + [BaseTile.PLATFORM.value] * 4
    + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 6,
)
end_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value]
    + [BaseTile.END.value]
    + [BaseTile.EMPTY.value] * 4,
    add_ons=[AddOn.NONE.value] * 6,
)

rows = deque(
    [
        Row.from_tile_lists(0, end_row),
        Row.from_tile_lists(1, basic_row),
        Row.from_tile_lists(2, basic_row),
        Row.from_tile_lists(3, basic_row),
        Row.from_tile_lists(4, basic_row),
        Row.from_tile_lists(5, start_row),
    ]
)


grid = Grid(
    n_rows=len(rows),
    n_cols=len(rows[0].tiles),
    rows=rows,
)

player = Player(pos=PlayerPosition(col=4, row=5, face_direction=PlayerDirection.UP))

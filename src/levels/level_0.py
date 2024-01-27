from collections import deque
from typing import List
from src.grid.grid import Grid
from src.grid.conveyer import Row, Conveyer, RowDefinition, ConveyerDirection
from src.grid.tile import *
from src.art.image import Image
from src.game import Player
from src.player.player import PlayerDirection

start_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value] * 8 + [BaseTile.START.value] + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 10,
)
basic_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value] + [BaseTile.PLATFORM.value] * 8 + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 10,
)
end_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value] + [BaseTile.END.value] + [BaseTile.EMPTY.value] * 8,
    add_ons=[AddOn.NONE.value] * 10,
)

rows = deque(
    [
        Row.from_tile_lists(0, end_row),
        Row.from_tile_lists(1, basic_row),
        Row.from_tile_lists(2, basic_row),
        Row.from_tile_lists(3, basic_row),
        Row.from_tile_lists(4, basic_row),
        Row.from_tile_lists(5, basic_row),
        Row.from_tile_lists(6, start_row),
    ]
)


grid = Grid(
    n_rows=len(rows),
    n_cols=len(rows[0].tiles),
    rows=rows,
)

player = Player(col=7, row=6, face_direction=PlayerDirection.UP)

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
    base_tiles=[BaseTile.EMPTY.value] * 8
    + [BaseTile.START.value]
    + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 10,
)
basic_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value]
    + [BaseTile.PLATFORM.value] * 8
    + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 10,
)
chest_row1 = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value]
    + [BaseTile.PLATFORM.value] * 8
    + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 3 + [AddOn.CHEST.value] + [AddOn.NONE.value] * 6,
)
chest_row2 = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value]
    + [BaseTile.PLATFORM.value] * 8
    + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 5 + [AddOn.CHEST.value] + [AddOn.NONE.value] * 4,
)
chest_row3 = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value]
    + [BaseTile.PLATFORM.value] * 8
    + [BaseTile.EMPTY.value],
    add_ons=[AddOn.NONE.value] * 8 + [AddOn.CHEST.value] + [AddOn.NONE.value] * 1,
)
end_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY.value]
    + [BaseTile.END.value]
    + [BaseTile.EMPTY.value] * 8,
    add_ons=[AddOn.NONE.value] * 10,
)

rows = deque(
    [
        Row.from_tile_lists(0, end_row),
        Row.from_tile_lists(1, chest_row1),
        Row.from_tile_lists(2, chest_row1),
        Row.from_tile_lists(3, chest_row3),
        Row.from_tile_lists(4, chest_row2),
        Row.from_tile_lists(5, chest_row1),
        Row.from_tile_lists(6, start_row),
    ]
)


grid = Grid(
    n_rows=len(rows),
    n_cols=len(rows[0].tiles),
    rows=rows,
)

player = Player(pos=PlayerPosition(col=8, row=6, face_direction=PlayerDirection.UP))

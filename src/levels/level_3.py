from collections import deque
from typing import List
from src.grid.grid import Grid
from src.grid.conveyer import Row, Conveyer, RowDefinition, PlayerDirection
from src.grid.tile import *
from src.art.image import Image
from src.game import Player
from src.player.player import PlayerDirection
from src.player.player_info import PlayerPosition

basic_row = RowDefinition(
    base_tiles= [BaseTile.PLATFORM.value] * 8,
    add_ons=[AddOn.NONE.value] * 8,
)
start_row = RowDefinition(
    base_tiles=[BaseTile.EMPTY] * 7 + [BaseTile.START],
    add_ons=[AddOn.NONE] * 8,
)
conv_row_4 = [AddOn.NONE] * 8
row_5 = RowDefinition(
    base_tiles=[BaseTile.PLATFORM.value] * 8,
    add_ons=[AddOn.NONE.value] * 2 + [AddOn.CHEST.value] + [AddOn.NONE.value] * 5,
)
conv_1 = [AddOn.NONE] * 7 + [AddOn.HOLE]
conv_2 = [AddOn.NONE] * 2 + [AddOn.CHEST] + [AddOn.NONE] * 5
conv_3 = [AddOn.NONE] * 3 + [AddOn.HOLE] + [AddOn.NONE] * 4
conv_4 = [AddOn.NONE] * 8
end_row = RowDefinition(
    base_tiles=[BaseTile.END] + [BaseTile.EMPTY] * 7,
    add_ons=[AddOn.NONE] * 8,
)

rows = deque(
    [
        Row.from_tile_lists(0, end_row),
        Conveyer.from_add_on_list(1, conv_1, direction=PlayerDirection.RIGHT),
        Conveyer.from_add_on_list(2, conv_2, direction=PlayerDirection.RIGHT),
        Conveyer.from_add_on_list(3, conv_3),
        Conveyer.from_add_on_list(4, conv_row_4, direction=PlayerDirection.RIGHT),
        Row.from_tile_lists(5, row_5),
        Row.from_tile_lists(6, start_row),
    ]
)


grid = Grid(
    n_rows=len(rows),
    n_cols=len(rows[0].tiles),
    rows=rows,
)

player = Player(pos=PlayerPosition(col=7, row=6, face_direction=PlayerDirection.UP))

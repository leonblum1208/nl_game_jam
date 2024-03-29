from collections import deque
from typing import List
from src.grid.grid import Grid
from src.grid.conveyer import Row, Conveyer, RowDefinition, PlayerDirection
from src.grid.tile import *
from src.art.image import Image
from src.game import Player
from src.player.player_info import PlayerDirection, PlayerPosition
from src.player.player import PlayerDirection


start_row = RowDefinition(
    base_tiles=[BaseTile.PLATFORM] * 3 + [BaseTile.START],
    add_ons=[AddOn.NONE] * 4,
)
conv_1 = [AddOn.NONE] * 3 + [AddOn.HOLE]
conv_2 = [AddOn.NONE, AddOn.CHEST, AddOn.NONE, AddOn.NONE]
conv_3 = [AddOn.HOLE] + [AddOn.NONE] * 3
conv_4 = [AddOn.NONE] * 4
end_row = RowDefinition(
    base_tiles=[BaseTile.END] + [BaseTile.PLATFORM] * 3,
    add_ons=[AddOn.NONE] * 4,
)

rows = deque(
    [
        Row.from_tile_lists(0, end_row),
        Conveyer.from_add_on_list(1, conv_4),
        Conveyer.from_add_on_list(2, conv_3, direction=PlayerDirection.RIGHT),
        Conveyer.from_add_on_list(3, conv_2),
        Conveyer.from_add_on_list(4, conv_1),
        Row.from_tile_lists(5, start_row),
    ]
)


grid = Grid(
    n_rows=len(rows),
    n_cols=len(rows[0].tiles),
    rows=rows,
)

player = Player(pos=PlayerPosition(col=3, row=5, face_direction=PlayerDirection.UP))

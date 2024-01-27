from collections import deque
from typing import List
from src.grid.grid import Grid
from src.grid.conveyer import Row, Conveyer, RowDefinition
from src.grid.tile import *


start_row = RowDefinition(
    base_tiles=[BaseTile.PLATFORM.value] * 3 + [BaseTile.START.value],
    add_ons=[AddOn.NONE.value] * 4,
)
conv_1 = [AddOn.NONE.value] * 4
conv_2 = [AddOn.NONE.value] * 4
conv_3 = [AddOn.NONE.value] * 4
conv_4 = [AddOn.NONE.value] * 4
end_row = RowDefinition(
    base_tiles=[BaseTile.END.value] + [BaseTile.PLATFORM.value] * 3,
    add_ons=[AddOn.NONE.value] * 4,
)

rows = deque(
    [
        Row.from_tile_lists(row=0, row_def=end_row),
        Conveyer.from_add_on_list(1, conv_4),
        Conveyer.from_add_on_list(2, conv_3),
        Conveyer.from_add_on_list(3, conv_2),
        Conveyer.from_add_on_list(4, conv_1),
        Row.from_tile_lists(row=5, row_def=start_row),
    ]
)


LEVEL_1 = Grid(
    n_rows=len(rows),
    n_cols=len(rows[0].tiles),
    rows=rows,
)

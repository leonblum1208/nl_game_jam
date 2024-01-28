from __future__ import annotations

from typing import List, Optional
import pygame
from pydantic import BaseModel
from enum import Enum
from src.art.arrow import Arrow
from src.player.player_info import PlayerDirection
from src.art.image import Image
from src.art.const import BODOS_IMAGES, MOVE_IMAGES, TURN_IMAGES
from src.art.color import *
from src.const import *
from pathlib import Path
from copy import deepcopy

from src.grid.grid import Grid
from src.grid.tile import AddOn, BaseTile
from src.player.player_info import PlayerDirection, PlayerPosition
from src.const import GameOver


class MovementInducer(Enum):
    CONVEYER: int = 1
    ANY: int = 0

class Movement(BaseModel):
    energy_cost: float = 1
    induced: MovementInducer = MovementInducer.ANY

    def execute(self, pos: PlayerPosition) -> None:
        raise NotImplementedError

    @property
    def image(self) -> Optional[Image]:
        return None


class PlayerTurn(Movement):
    energy_cost: float = 1
    turn_direction: int

    def execute(self, pos: PlayerPosition) -> PlayerPosition:
        face_direction = PlayerDirection(
            (pos.face_direction.value + self.turn_direction) % 4
        )
        return PlayerPosition(col=pos.col, row=pos.row, face_direction=face_direction)
    @property
    def image(self) -> Optional[Image]:
        return TURN_IMAGES[self.turn_direction]

class PlayerMove(Movement):
    energy_cost: float = 2
    step: int

    def execute(self, pos: PlayerPosition) -> PlayerPosition:
        if pos.face_direction == PlayerDirection.RIGHT:
            col = pos.col - self.step
            row = pos.row
        elif pos.face_direction == PlayerDirection.LEFT:
            col = pos.col + self.step
            row = pos.row
        elif pos.face_direction == PlayerDirection.UP:
            col = pos.col
            row = pos.row - self.step
        else:
            col = pos.col
            row = pos.row + self.step

        return PlayerPosition(col=col, row=row, face_direction=pos.face_direction)

    @property
    def image(self) -> Optional[Image]:
        return MOVE_IMAGES[self.step]

class PlayerForceMove(Movement):
    energy_cost: float = 0
    step: int
    direction: PlayerDirection

    def execute(self, pos: PlayerPosition) -> PlayerPosition:
        col, row = pos.col, pos.row
        if self.direction == PlayerDirection.RIGHT:
            col += self.step
        elif self.direction == PlayerDirection.LEFT:
            col -= self.step
        elif self.direction == PlayerDirection.UP:
            row -= self.step
        else:
            row += self.step
        return PlayerPosition(col=col, row=row, face_direction=pos.face_direction)


class Player(BaseModel):
    size: int = 0.8
    pos: PlayerPosition
    energy: int = 0
    movement_history: List[List[Movement]] = []
    pos_history: List[List[PlayerPosition]] = []
    grid_history: List[List[Grid]] = []

    @property
    def image(self) -> Image:
        return BODOS_IMAGES[self.pos.face_direction]

    def handle_movement(self, player_movements: List[Movement], grid: Grid):
        movements_done, positions_occupied, turn_grids = [], [], []
        player_movements_rev = list(reversed(player_movements))
        while player_movements_rev:
            player_movement = player_movements_rev.pop()
            turn_movements = [player_movement]
            conveyers_moved = False
            while turn_movements:
                movement = turn_movements.pop()
                new_pos = movement.execute(self.pos)
                movement_tile = grid.get_tile(new_pos)
                movements_done.append(movement)
                positions_occupied.append(new_pos)
                turn_grids.append(deepcopy(grid))
                if movement_tile.add_on_type == AddOn.HOLE:
                    raise GameOver("You fell into a hole.")
                if movement_tile.base_type == BaseTile.EMPTY:
                    raise GameOver("You tried to walk on nothing")
                if movement_tile.add_on_type == AddOn.CHEST:
                    direction = PlayerDirection.get_direction_from_positions(
                        start=self.pos, end=new_pos
                    )
                    turn_movements.append(
                        PlayerForceMove(step=1, direction=direction.opposite)
                    )
                    print("Walked into chest")
                self.pos = new_pos
                # handle conveyers
                if not conveyers_moved and len(turn_movements) == 0:
                    current_tile = grid.get_tile(self.pos)
                    if current_tile.base_type == BaseTile.CONVEYER:
                        direction = grid.rows[self.pos.row].direction
                        steps = grid.rows[self.pos.row].speed
                        turn_movements.append(
                            PlayerForceMove(step=steps, direction=direction, induced=MovementInducer.CONVEYER)
                        )
                    grid.update(1)
                    conveyers_moved = True

        self.movement_history.append(movements_done)
        self.pos_history.append(positions_occupied)
        self.grid_history.append(turn_grids)

    def draw(self, screen, pos: PlayerPosition):
        scaled_image_surface = self.image.scale(self.size)
        scaled_image_rect = scaled_image_surface.get_rect()
        scaled_image_rect.topleft = (
            pos.col * TILE_WIDTH_PIX
            + (TILE_WIDTH_PIX - scaled_image_rect.width) / 2,
            pos.row * TILE_HEIGHT_PIX
            + (TILE_HEIGHT_PIX - scaled_image_rect.height) / 2,
        )
        screen.blit(scaled_image_surface, scaled_image_rect)

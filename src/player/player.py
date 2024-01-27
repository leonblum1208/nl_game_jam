from __future__ import annotations

from typing import List
import pygame
from pydantic import BaseModel
from enum import Enum
from src.art.arrow import Arrow
from src.art.image import Image
from src.art.color import *
from src.const import *
from pathlib import Path

from src.grid.grid import Grid
from src.grid.tile import AddOn
from src.player.player_info import PlayerDirection, PlayerPosition


class GameOver(Exception):
    pass


class Movement(BaseModel):
    energy_cost: float = 1

    def execute(self, pos: PlayerPosition) -> None:
        raise NotImplementedError


class PlayerTurn(Movement):
    turn_direction: int

    def execute(self, pos: PlayerPosition) -> PlayerPosition:
        face_direction = PlayerDirection(
            (pos.face_direction.value + self.turn_direction) % 4
        )
        return PlayerPosition(col=pos.col, row=pos.row, face_direction=face_direction)


class PlayerMove(Movement):
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
            row = pos.row + self.step
        else:
            col = pos.col
            row = pos.row - self.step
        
        return PlayerPosition(col=col, row=row, face_direction=pos.face_direction)


class Player(BaseModel):
    size: int = 0.8
    pos: PlayerPosition
    energy: int = 0
    movement_history: List[Movement] = []
    pos_history: List[PlayerPosition] = []

    @property
    def image(self) -> Image:
        return Image(image_name=f"Robo-{self.pos.face_direction.name}.png")

    def handle_movement(self, movements: List[Movement], grid: Grid):
        for movement in movements:
            new_pos = movement.execute(self.pos)
            movement_tile = grid.get_tile(new_pos)

            if movement_tile.add_on_type == AddOn.HOLE:
                raise GameOver()
            if movement_tile.add_on_type == AddOn.CHEST:
                new_pos = self.pos
                print("Walked into chest")
            self.pos = new_pos
            self.movement_history.append(movement)
            self.pos_history.append(new_pos)

    def draw(self, screen):
        image_surface = self.image.load()
        image_rect = image_surface.get_rect()
        scaled_image_surface = self.image.scale(image_surface, image_rect, self.size)
        scaled_image_rect = scaled_image_surface.get_rect()
        scaled_image_rect.topleft = (
            self.pos.col * TILE_WIDTH_PIX + (TILE_WIDTH_PIX - scaled_image_rect.width) / 2,
            self.pos.row * TILE_HEIGHT_PIX
            + (TILE_HEIGHT_PIX - scaled_image_rect.height) / 2,
        )
        screen.blit(scaled_image_surface, scaled_image_rect)
        # pos_x = self.col * TILE_WIDTH_PIX + (TILE_WIDTH_PIX - self.width)/2
        # pos_y = self.row * TILE_HEIGHT_PIX + (TILE_HEIGHT_PIX - self.height) / 2
        # pygame.draw.rect(screen, color, (pos_x, pos_y, self.width, self.height))
        # self.arrow.draw(screen,pos_x, pos_y)

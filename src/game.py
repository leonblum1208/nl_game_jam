from typing import List
import pygame
import sys
from pydantic import BaseModel
from src.grid.grid import Grid
from src.player.player import Player, PlayerMove, PlayerTurn, Movement
from src.grid.grid import Grid


class Game(BaseModel):
    player: Player
    grid: Grid
    movements: List[Movement] = []

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.movements.append(PlayerTurn(turn_direction=-1))
                elif event.key == pygame.K_RIGHT:
                    self.movements.append(PlayerTurn(turn_direction=1))
                elif event.key == pygame.K_UP:
                    self.movements.append(PlayerMove(step=-1))
                elif event.key == pygame.K_DOWN:
                    self.movements.append(PlayerMove(step=1))
                elif event.key == pygame.K_r:
                    self.player.handle_movement(player_movements=self.movements, grid=self.grid)
                    self.movements = []

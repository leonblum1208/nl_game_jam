import pygame
import sys
from pydantic import BaseModel
from src.grid.grid import Grid
from src.player.player import Player, PlayerMove, PlayerTurn
from src.grid.grid import Grid


class Game(BaseModel):
    player: Player
    grid: Grid

    def handle_event(self):
        movements = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movements.append(PlayerTurn(turn_direction=-1))
                elif event.key == pygame.K_RIGHT:
                    movements.append(PlayerTurn(turn_direction=1))
                elif event.key == pygame.K_UP:
                    movements.append(PlayerMove(step=-1))
                elif event.key == pygame.K_DOWN:
                    movements.append(PlayerMove(step=1))
                elif event.key == pygame.K_r:
                    self.grid.update(turns=1)
        self.player.handle_movement(movements=movements, grid=self.grid)

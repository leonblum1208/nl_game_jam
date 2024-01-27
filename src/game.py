import pygame
import sys
from pydantic import BaseModel
from src.grid.grid import Grid
from src.player.player import Player
from src.grid.grid import Grid


class Game(BaseModel):
    player: Player
    grid: Grid

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.turn(-1)
                elif event.key == pygame.K_RIGHT:
                    self.player.turn(1)
                elif event.key == pygame.K_UP:
                    self.player.move(1)
                elif event.key == pygame.K_DOWN:
                    self.player.move(-1)
                elif event.key == pygame.K_r:
                    self.grid.update(turns=1)

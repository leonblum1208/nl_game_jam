from typing import List
import pygame
import sys
from pydantic import BaseModel
from src.grid.grid import Grid
from src.player.player import Player, PlayerMove, PlayerTurn, Movement
from src.grid.grid import Grid
from copy import deepcopy
from src.const import *


class Game(BaseModel):
    player: Player
    grid: Grid
    movements: List[Movement]
    num_pos_sets: int = 0
    game_over_messages: List[GameOverMessage] = []

    @classmethod
    def from_player_and_grid(cls, player: Player, grid: Grid) -> "Game":
        return cls(player=deepcopy(player), grid=deepcopy(grid), movements=[])

    def handle_event(self):
        self.game_over_messages = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.movements.append(PlayerTurn(turn_direction=-1))
                elif event.key == pygame.K_d:
                    self.movements.append(PlayerTurn(turn_direction=1))
                elif event.key == pygame.K_w:
                    self.movements.append(PlayerMove(step=1))
                elif event.key == pygame.K_s:
                    self.movements.append(PlayerMove(step=-1))
                elif event.key == pygame.K_q:
                    self.movements.append(PlayerMove(step=0))
                elif event.key == pygame.K_BACKSPACE:
                    if self.movements:
                        self.movements.pop()
                elif event.key == pygame.K_RETURN:
                    self.player.handle_movement(
                        player_movements=self.movements, grid=self.grid, game_over_messages=self.game_over_messages
                    )
                    self.movements = []
            if self.game_over_messages:
                raise GameOver()

    def draw_movements(self, screen):
        images_drawn = 0
        for movement in self.movements:
            image = movement.image
            if image:
                scaled_image_surface = image.scale(0.35)
                scaled_image_rect = scaled_image_surface.get_rect()
                scaled_image_rect.topleft = (WIDTH - scaled_image_rect.width, images_drawn * (scaled_image_rect.height * 1.05))
                screen.blit(scaled_image_surface, scaled_image_rect)
                images_drawn += 1

import pygame
import sys
from src.game import Game
from src.art.color import *
from src.const import *
from src.grid.grid import Grid
from src.grid.tile import BaseTile
from src.player.player import Player
from src.const import GameOver
from src.levels import level_0, level_1, level_2, level_3, level_firstDraft
import time
from copy import deepcopy


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Rectangle")

game_over_banner = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
game_over_banner.fill((0, 0, 0, 192))

# Set up the game
cur_level = level_2
game = Game.from_player_and_grid(player=cur_level.player, grid=cur_level.grid)

game_over_flag = False
# Game loop
while True:
    try:
        game.handle_event()
    except GameOver as e:
        game_over_flag = True

    if len(game.player.pos_history) > game.num_pos_sets:
        game.num_pos_sets += 1
        for pos, sub_grid in zip(game.player.pos_history[-1], game.player.grid_history[-1]):
            screen.fill(BLACK)
            sub_grid.draw(screen=screen)
            game.player.draw(screen=screen, pos=pos)
            pygame.display.flip()
            print(pos)
            time.sleep(0.2)
    screen.fill(BLACK)
    game.grid.draw(screen=screen)
    game.draw_movements(screen=screen)
    game.player.draw(screen=screen, pos=game.player.pos)

    if game.grid.get_tile(game.player.pos).base_type.value == BaseTile.END:
        print("Success")

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
    if game.game_over_messages:
        last_msg = game.game_over_messages[-1]
        if last_msg.type == MessageType.FAIL:
            screen.blit(game_over_banner, (0, 0))
            pygame.display.flip()
            font = pygame.font.Font(None, 50)
            text1 = font.render(f"GAME OVER! {last_msg.message}", True, WHITE)
            text2 = font.render(f"Press R to restart", True, WHITE)
            text3 = font.render(f"Press Q to quit", True, WHITE)
            for row, text in enumerate((text1, text2, text3)):
                screen.blit(
                    text,
                    (
                        WIDTH // 2 - text.get_width() // 2,
                        (HEIGHT // 2 - text.get_height() // 2)
                        + text.get_height() * row * 1.5,
                    ),
                )
            pygame.display.flip()
            while game_over_flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (
                        event.type == pygame.KEYDOWN and event.key == pygame.K_q
                    ):
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        game = Game.from_player_and_grid(
                            player=cur_level.player, grid=cur_level.grid
                        )
                        game_over_flag = False
        elif last_msg.type == MessageType.SUCCESS:
            screen.blit(game_over_banner, (0, 0))
            pygame.display.flip()
            font = pygame.font.Font(None, 50)
            text0 = font.render(f"CONGRATULATIONS! {last_msg.message}", True, WHITE)
            text001 = font.render(f"", True, WHITE)
            text01 = font.render(f"SCORE: {int(game.player.score)}", True, WHITE)
            text1 = font.render(f"Net Energy Usage:{int(game.player.net_energy_usage)} - Num. Movements:{game.player.n_movements}", True, WHITE)
            text12 = font.render(f"", True, WHITE)
            text2 = font.render(f"Press R to restart", True, WHITE)
            text3 = font.render(f"Press Q to quit", True, WHITE)
            for row, text in enumerate((text0, text001, text01,  text1, text12, text2, text3)):
                screen.blit(
                    text,
                    (
                        WIDTH // 2 - text.get_width() // 2,
                        (HEIGHT/2 // 2 - text.get_height() // 2)
                        + text.get_height() * row * 1.5,
                    ),
                )
            pygame.display.flip()
            while game_over_flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (
                        event.type == pygame.KEYDOWN and event.key == pygame.K_q
                    ):
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        game = Game.from_player_and_grid(
                            player=cur_level.player, grid=cur_level.grid
                        )
                        game_over_flag = False

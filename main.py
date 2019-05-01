import pygame
from game_functions import *

def run_game():
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tic-Tac-Toe')

    cells = create_cells(screen)

    is_game_ended = False
    while True:
        is_game_ended = check_events(cells)
        pygame.display.flip()

try:
    run_game()
except Exception as e:
    print(e)
    sys.exit()

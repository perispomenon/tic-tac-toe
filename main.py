import pygame
from game_functions import *

def run_game():
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tic-Tac-Toe')

    cells = create_cells(screen)

    while True:
        check_events(cells)
        check_game_end(cells)
        pygame.display.flip()

try:
    run_game()
except Exception as e:
    print(e)
    sys.exit()

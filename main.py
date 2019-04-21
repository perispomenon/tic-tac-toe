import pygame
from game_functions import *

def run_game():
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tic-Tac-Toe')

    while True:
        check_events()
        pygame.display.flip()


run_game()

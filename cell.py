import pygame
from pygame.sprite import Sprite
from turn import Turn

class Cell(Sprite):
    def __init__(self, screen, coords):
        super().__init__()
        self.color = 222, 222, 222
        self.sign_color = 55, 55, 55
        self.coords = coords
        self.screen = screen
        self.sign = None
        self.rect = pygame.Rect(coords['left'], coords['top'], coords['size'], coords['size'])
        pygame.draw.rect(self.screen, self.color, self.rect)

    def fill(self, turn):
        self.sign = turn
        if turn == Turn.CROSSES:
            self.__draw_cross()
        else:
            self.__draw_nought()

    def is_togglable(self):
        return self.sign == None

    def __draw_cross(self):
        start_pos = self.coords['left'] + 20, self.coords['top'] + 20
        end_pos = self.coords['left'] + self.coords['size'] - 20, self.coords['top'] + self.coords['size'] - 20
        pygame.draw.line(self.screen, self.sign_color, start_pos, end_pos, 10)

        start_pos = self.coords['left'] + self.coords['size'] - 20, self.coords['top'] + 20
        end_pos = self.coords['left'] + 20, self.coords['top'] + self.coords['size'] - 20
        pygame.draw.line(self.screen, self.sign_color, start_pos, end_pos, 10)

    def __draw_nought(self):
        rect = pygame.Rect(self.coords['left'] + 10, self.coords['top'] + 10, self.coords['size'] - 20, self.coords['size'] - 20)
        pygame.draw.ellipse(self.screen, self.sign_color, rect, 10)

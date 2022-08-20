import pygame 
from .constants import SQUARE_SIZE

class Piece:
    PADDING = 10
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = (SQUARE_SIZE * self.col) + (SQUARE_SIZE // 2)
        self.y = (SQUARE_SIZE * self.row) + (SQUARE_SIZE // 2)

    def draw(self, win):
        radius = (SQUARE_SIZE // 2) - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)        

    def __repr__(self):
        return str(self.color)
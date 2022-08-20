import pygame
from .constants import HEIGTH, WIDTH, ROWS, COLS, COLOR_WHITE, COLOR_BLACK
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.white_left = 2
        self.black_left = 2
        self.create_board()
 
    def drawGrid(self, win):
        size = WIDTH // ROWS
        x = 0
        y = 0
        for i in range(ROWS - 1):
            x = x + size
            y = y + size
            pygame.draw.line(win, COLOR_BLACK, (x, 0), (x, HEIGTH))
            pygame.draw.line(win, COLOR_BLACK, (0, y), (HEIGTH, y))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

        self.board[2][2] = Piece(2, 2, COLOR_WHITE)
        self.board[2][3] = Piece(2, 3, COLOR_BLACK)
        self.board[3][2] = Piece(3, 2, COLOR_BLACK)
        self.board[3][3] = Piece(3, 3, COLOR_WHITE)

    def draw(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    

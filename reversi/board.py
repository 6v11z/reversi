import pygame
from .constants import HEIGTH, WIDTH, ROWS, COLS, COLOR_WHITE, COLOR_BLACK
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.white_count = 2
        self.black_count = 2
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

        self.board[(ROWS // 2) - 1][(ROWS // 2) - 1] = Piece((ROWS // 2) - 1, (ROWS // 2) - 1, COLOR_WHITE)
        self.board[(ROWS // 2) - 1][(ROWS // 2)] = Piece((ROWS // 2) - 1, (ROWS // 2), COLOR_BLACK)
        self.board[(ROWS // 2)][(ROWS // 2) - 1] = Piece((ROWS // 2), (ROWS // 2) - 1, COLOR_BLACK)
        self.board[(ROWS // 2)][(ROWS // 2)] = Piece((ROWS // 2), (ROWS // 2), COLOR_WHITE)

    def draw(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def add_piece(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = Piece(row, col, COLOR_BLACK)

    def get_valid_moves():
        pass
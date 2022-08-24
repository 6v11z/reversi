import pygame

from reversi.piece import Piece
from .constants import COLOR_BLACK, COLOR_WHITE
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.board = Board()
        self.turn = COLOR_BLACK
        self.valid_moves = {}

    def update(self):
        self.board.drawGrid(self.win)
        self.board.draw(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        pass

    def _move(self, row, col):
        if self.board[row][col] == 0 and (row, col) in self.valid_moves:
            self.board.add_piece(row, col)

    def change_turn(self):
        if self.turn == COLOR_BLACK:
            self.turn = COLOR_WHITE
        else:
            self.turn = COLOR_BLACK
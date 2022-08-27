import pygame

from reversi.piece import Piece
from .constants import COLOR_BLACK, COLOR_WHITE, COLOR_GREEN, SQUARE_SIZE, WIDTH, SCORE_WIDTH, SCORE_HEIGHT
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.turn = COLOR_BLACK
        self.board = Board()
        self.valid_moves = []

    def update(self):
        self.win.fill(COLOR_GREEN)
        self.board.draw_grid(self.win)
        self.board.draw_scores(self.win)
        self.board.draw(self.win)
        # Usar condicional cuando ya tenga implementada la IA
        # if (self.turn == COLOR_BLACK):
        #     self.draw_valid_moves()
        self.draw_valid_moves()
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, move):
        row = move[0]
        col = move[1]
        if (self.board.is_valid_move(row, col, self.turn)):
            self.board.make_move(row, col, self.turn)
            self.change_turn()

    def draw_valid_moves(self):
        valid_moves = self.board.get_valid_moves(self.turn)
        for move in valid_moves:
            row = move[0]
            col = move[1]
            pygame.draw.circle(self.win, self.turn, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 5)

    def winner(self):
        return self.board.winner()
        
    def change_turn(self):
        if (self.turn == COLOR_BLACK):
            self.turn = COLOR_WHITE
        else:
            self.turn = COLOR_BLACK
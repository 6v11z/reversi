import pygame
from .constants import HEIGTH, WIDTH, COLS, ROWS, COLOR_WHITE, COLOR_BLACK, DIRECTIONS
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.white_count = 2
        self.black_count = 2
        self.empty_count = (ROWS * COLS) - (self.white_count + self.black_count)
        self.create_board()

    # Dibuja las lineas del tablero
    def drawGrid(self, win):
        size = WIDTH // ROWS
        x = 0
        y = 0
        for i in range(ROWS - 1):
            x = x + size
            y = y + size
            pygame.draw.line(win, COLOR_BLACK, (x, 0), (x, HEIGTH))
            pygame.draw.line(win, COLOR_BLACK, (0, y), (HEIGTH, y))

    # Inicializa el tablero con los cuatro piezas iniciales
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(ROWS):
                self.board[row].append(0)

        self.board[(ROWS // 2) - 1][(ROWS // 2) - 1] = Piece((ROWS // 2) - 1, (ROWS // 2) - 1, COLOR_WHITE)
        self.board[(ROWS // 2) - 1][(ROWS // 2)] = Piece((ROWS // 2) - 1, (ROWS // 2), COLOR_BLACK)
        self.board[(ROWS // 2)][(ROWS // 2) - 1] = Piece((ROWS // 2), (ROWS // 2) - 1, COLOR_BLACK)
        self.board[(ROWS // 2)][(ROWS // 2)] = Piece((ROWS // 2), (ROWS // 2), COLOR_WHITE)

    # Dibuja la pieza en el tablero
    def draw(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if (piece != 0):
                    piece.draw(win)
    
    def is_valid_move(self, row, col, turn):
        if (self.board[row][col] != 0):
            return False
    
        self.board[row][col] = str(turn)
    
        if (str(turn) == str(COLOR_BLACK)):
            other_tile = str(COLOR_WHITE)
        else:
            other_tile = str(COLOR_BLACK)
    
        tiles_to_flip = []
        for direction in DIRECTIONS:
            x, y = row, col
            x_dir = direction[0]
            y_dir = direction[1]
            x += x_dir
            y += y_dir
            if ((self.is_on_board(x, y) )and (str(self.board[x][y]) == other_tile)):
                x += x_dir
                y += y_dir
                if (not self.is_on_board(x, y)):
                    continue
                while str(self.board[x][y]) == other_tile:
                    x += x_dir
                    y += y_dir
                    if (not self.is_on_board(x, y)):
                        break
                if (not self.is_on_board(x, y)):
                    continue
                if (str(self.board[x][y]) == str(turn)):
                    while True:
                        x -= x_dir
                        y -= y_dir
                        if ((x == row) and (y == col)):
                            break
                        tiles_to_flip.append([x, y])
    
        self.board[row][col] = 0
        if len(tiles_to_flip) == 0:
            return False
        return tiles_to_flip
        
    def add_piece(self, row, col, color):
        if self.board[row][col] == 0:
            self.board[row][col] = Piece(row, col, color)
            if color == COLOR_BLACK:
                self.black_count += 1
            else:
                self.white_count += 1

    # Retorna: Booleano (True si el juego acabo, False en caso contrario)
    def is_game_end(self):
        if ((self.get_valid_moves(COLOR_BLACK) == []) or (self.get_valid_moves(COLOR_WHITE) == [])):
            return True

        return False

    def winner(self):
        if ((self.black_count < self.white_count) and (self.is_game_end() == True)):
            return "Ha ganado el jugador blanco"

        if ((self.black_count > self.white_count) and (self.is_game_end() == True)):
            return "Ha ganado el jugador negro"

        if ((self.black_count == self.white_count) and (self.is_game_end() == True)):
            return "Empate"

        return None

    # Retorna: booleano
    # Revisa si la fila y la columna estan dentro del tablero
    def is_on_board(self, row, col):
        return ((row >= 0) and (row <= ROWS - 1)) and ((col >= 0) and (col <= COLS - 1))

    # Retorna: lista
    # Devuelve todos los movimientos validos para el turno del jugador
    def get_valid_moves(self, turn):
        valid_moves = []
 
        for row in range(ROWS):
            for col in range(COLS):
                move = (row, col)
                if (self.is_valid_move(row, col, turn)):
                    valid_moves.append(move)
        return valid_moves

    def make_move(self, row, col, turn):
        tiles_to_flip = self.is_valid_move(row, col, turn)
        if tiles_to_flip == False:
            return False
    
        self.board[row][col] = Piece(row, col, turn)
        for tile in tiles_to_flip:
            x = tile[0]
            y = tile[1]
            self.board[x][y] = Piece(x, y, turn)
        self.update_tiles_count()
        return True

    def update_tiles_count(self):
        black_count = 0
        white_count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (str(self.board[row][col]) == str((0, 0, 0))):
                    black_count += 1
                if (str(self.board[row][col]) == str((255, 255, 255))):
                    white_count += 1
        self.black_count = black_count
        self.white_count = white_count
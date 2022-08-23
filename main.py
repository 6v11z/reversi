import pygame
from reversi.board import Board
from reversi.constants import COLOR_BLACK, SQUARE_SIZE, WIDTH, HEIGTH, COLOR_GREEN, ROWS
from reversi.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
WIN.fill(COLOR_GREEN)
pygame.display.set_caption("Reversi")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = int(y // SQUARE_SIZE)
    col = int(x // SQUARE_SIZE)
    return (row, col)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = get_row_col_from_mouse(pygame.mouse.get_pos())
                row = pos[0]
                col = pos[1]
                # board.add_piece(row, col)
        game.update()

    pygame.quit()
 
if __name__ == "__main__":
    main()
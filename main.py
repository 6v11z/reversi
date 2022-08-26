import pygame
from reversi.board import Board
from reversi.constants import COLOR_BLACK, SQUARE_SIZE, WIDTH, HEIGTH, COLOR_GREEN, ROWS
from reversi.game import Game
import time

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Reversi")

def get_row_col_from_mouse(pos):
    x = pos[0] 
    y = pos[1]
    row = int(y // SQUARE_SIZE)
    col = int(x // SQUARE_SIZE)
    return (row, col)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)

        if (game.winner() != None):
            print(game.winner())
            time.sleep(10)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = get_row_col_from_mouse(pygame.mouse.get_pos())
                game.select(pos)

            # Opcion para reiniciar el juego con la tecla R
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_r:
            #         game.reset()

        game.update()

    pygame.quit()
 
if __name__ == "__main__":
    main()
import pygame
from reversi.board import Board
from reversi.constants import COLOR_BLACK, SCREEN_HEIGHT, SQUARE_SIZE, SCREEN_WIDTH, SCORE_HEIGHT, WIDTH, SCORE_WIDTH
from reversi.game import Game
import time

FPS = 60
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
            print(f"|| {game.winner()} ||")
            time.sleep(3)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[1] >= 600:
                    continue
                pos = get_row_col_from_mouse(pos)
                game.select(pos)

            # Opcion para reiniciar el juego con la tecla R
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_r:
            #         game.reset()

        game.update()

    pygame.quit()
 
if __name__ == "__main__":
    main()
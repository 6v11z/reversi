import pygame
from reversi.board import Board
from reversi.constants import WIDTH, HEIGTH, COLOR_GREEN

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
WIN.fill(COLOR_GREEN)
pygame.display.set_caption("Reversi")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
        board.drawGrid(WIN)
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()
 
if __name__ == "__main__":
    main()
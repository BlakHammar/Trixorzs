import pygame
import sys
from game import Game

# Initialize the game
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle Puzzle Game")

# Game Loop
def main():
    clock = pygame.time.Clock()
    game = Game(screen)
    while True:
        screen.fill((30, 30, 30))  # Background color
        game.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


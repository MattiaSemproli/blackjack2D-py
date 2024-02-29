import pygame
import sys
from BlackJack import BlackjackGame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w * 0.9
SCREEN_HEIGHT = screen_info.current_h * 0.85
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack")

if __name__ == "__main__":
    game = BlackjackGame(screen)
    game.run()

pygame.quit()
sys.exit()

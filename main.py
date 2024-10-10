import pygame
from board import Board
from player import Player
from dice import Dice

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ludo Game')

# Set up the clock
clock = pygame.time.Clock()
FPS = 30

# Initialize game components
board = Board(SCREEN_WIDTH, SCREEN_HEIGHT)
players = [Player("Red", board), Player("Blue", board)]  # Two players for now
dice = Dice()

# Main game loop
current_player = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if dice.is_dice_click(event.pos):
                roll_value = dice.roll()
                players[current_player].move(roll_value)
                current_player = (current_player + 1) % len(players)

    # Draw everything
    screen.fill((255, 255, 255))  # White background
    board.draw(screen)
    dice.draw(screen)
    
    for player in players:
        player.draw(screen)

    pygame.display.update()

    # Limit FPS
    clock.tick(FPS)

pygame.quit()

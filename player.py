import pygame

class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.position = 0  # Start position

    def move(self, steps):
        self.position += steps  # Simple linear movement

    def draw(self, screen):
        # Just drawing a circle on the board based on position for now
        row = self.position // len(self.board.grid[0])
        col = self.position % len(self.board.grid[0])
        center_x = col * self.board.cell_size + self.board.cell_size // 2
        center_y = row * self.board.cell_size + self.board.cell_size // 2
        pygame.draw.circle(screen, pygame.Color(self.color), (center_x, center_y), 20)

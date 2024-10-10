import pygame

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 50  # Size of each cell on the board
        self.grid = self.create_board()

    def create_board(self):
        rows = cols = self.width // self.cell_size
        return [[None for _ in range(cols)] for _ in range(rows)]

    def draw(self, screen):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # Draw grid lines

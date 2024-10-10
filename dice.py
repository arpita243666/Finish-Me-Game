import pygame
import random

class Dice:
    def __init__(self):
        self.value = 1
        self.rect = pygame.Rect(500, 50, 50, 50)  # Position of the dice on the screen

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

    def is_dice_click(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(text, (self.rect.x + 15, self.rect.y + 10))


import pygame
import random

# Constants
CELL_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FOOD_COLOR = (255, 0, 0)

class Food:
    def __init__(self):
        self.position = self.place_food([])

    def place_food(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, (*self.position, CELL_SIZE, CELL_SIZE))

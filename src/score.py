import pygame

# Constants
FONT_SIZE = 36
FONT_COLOR = (255, 255, 255)

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, FONT_SIZE)

    def update(self):
        self.score += 1

    def draw(self, screen):
        score_surface = self.font.render(f"Score: {self.score}", True, FONT_COLOR)
        screen.blit(score_surface, (10, 10))

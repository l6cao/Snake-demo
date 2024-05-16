import pygame
import sys
from snake import Snake
from food import Food
from score import Score

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
FPS_LEVELS = {'Easy': 10, 'Medium': 15, 'Hard': 20}

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        self.running = False
        self.fps = FPS_LEVELS['Medium']

    def start_menu(self):
        while True:
            self.screen.fill(BG_COLOR)
            self.display_message("Snake Game", 50, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.display_message("Press 1 for Easy", 35, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.display_message("Press 2 for Medium", 35, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            self.display_message("Press 3 for Hard", 35, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
            self.display_message("Press Enter to Start", 35, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.fps = FPS_LEVELS['Easy']
                    elif event.key == pygame.K_2:
                        self.fps = FPS_LEVELS['Medium']
                    elif event.key == pygame.K_3:
                        self.fps = FPS_LEVELS['Hard']
                    elif event.key == pygame.K_RETURN:
                        self.running = True
                        self.food = Food()  # Ensure food is placed before starting
                        return

    def display_message(self, text, size, position):
        font = pygame.font.SysFont(None, size)
        message = font.render(text, True, (255, 255, 255))
        rect = message.get_rect(center=position)
        self.screen.blit(message, rect)

    def run(self):
        self.start_menu()
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)

    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.game_over()
        if self.snake.eat_food(self.food.position):
            self.snake.grow()
            self.food.position = self.food.place_food(self.snake.body)
            self.score.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.fps)

    def game_over(self):
        self.running = False
        self.show_game_over_screen()

    def show_game_over_screen(self):
        while True:
            self.screen.fill(BG_COLOR)
            self.display_message(f"Game Over! Your Score: {self.score.score}", 50, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.display_message("Press Enter to Return to Main Menu", 35, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.snake = Snake()
                        self.food = Food()
                        self.score = Score()
                        self.start_menu()
                        return

if __name__ == "__main__":
    game = Game()
    game.run()

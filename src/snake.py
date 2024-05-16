import pygame

# Constants
CELL_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SNAKE_COLOR = (0, 255, 0)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = pygame.K_RIGHT
        self.growing = False

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = key
        elif key == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = key
        elif key == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = key
        elif key == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = key

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == pygame.K_UP:
            new_head = (head_x, head_y - CELL_SIZE)
        elif self.direction == pygame.K_DOWN:
            new_head = (head_x, head_y + CELL_SIZE)
        elif self.direction == pygame.K_LEFT:
            new_head = (head_x - CELL_SIZE, head_y)
        else:
            new_head = (head_x + CELL_SIZE, head_y)

        # Wrap around the screen
        new_head = (new_head[0] % SCREEN_WIDTH, new_head[1] % SCREEN_HEIGHT)

        self.body = [new_head] + self.body[:-1]
        if self.growing:
            self.body.append(self.body[-1])
            self.growing = False

    def grow(self):
        self.growing = True

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def eat_food(self, food_position):
        return self.get_head_position() == food_position

    def get_head_position(self):
        return self.body[0]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (*segment, CELL_SIZE, CELL_SIZE))

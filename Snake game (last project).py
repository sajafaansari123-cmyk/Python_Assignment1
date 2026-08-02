import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 10

# Font
font = pygame.font.SysFont(None, 35)


def draw_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))


def game():

    snake = [(100, 100)]
    direction = "RIGHT"

    food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)

    score = 0

    running = True

    while running:

        # Events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"

                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"

                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Head Position
        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= BLOCK_SIZE

        elif direction == "DOWN":
            head_y += BLOCK_SIZE

        elif direction == "LEFT":
            head_x -= BLOCK_SIZE

        elif direction == "RIGHT":
            head_x += BLOCK_SIZE

        new_head = (head_x, head_y)

        # Wall Collision
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            break

        # Self Collision
        if new_head in snake:
            break

        snake.insert(0, new_head)

        # Food Collision
        if head_x == food_x and head_y == food_y:

            score += 1

            food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)

        else:
            snake.pop()

        # Draw
        screen.fill(WHITE)

        pygame.draw.rect(
            screen,
            RED,
            (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE)
        )

        for block in snake:
            pygame.draw.rect(
                screen,
                GREEN,
                (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
            )

        draw_score(score)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    game()
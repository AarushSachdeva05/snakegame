import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Set the initial position and direction of the snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"

# Set the initial position of the food
food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
food_spawned = True

# Set the initial score
score = 0

# Set the game over flag
game_over = False

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Update the snake's position based on the direction
    if direction == "UP":
        snake_pos[1] -= 10
    elif direction == "DOWN":
        snake_pos[1] += 10
    elif direction == "LEFT":
        snake_pos[0] -= 10
    elif direction == "RIGHT":
        snake_pos[0] += 10

    # Check for collision with the food
    if snake_pos == food_pos:
        score += 1
        food_spawned = False

    # Create a new food if necessary
    if not food_spawned:
        food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
        food_spawned = True

    # Update the snake's body
    snake_body.insert(0, list(snake_pos))
    if len(snake_body) > score + 1:
        del snake_body[-1]

    # Check for collision with the snake's body
    if snake_pos in snake_body[1:]:
        game_over = True

    # Clear the screen
    window.fill(BLACK)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(15)

# Quit Pygame
pygame.quit()

import pygame
import time
import random

# Initial snake speed
snake_speed = 10

# Window size
window_x = 1000
window_y = 500

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Set game window
pygame.display.set_caption('Snake Game with Levels & Timed Food')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Snake initial position
snake_position = [100, 50]

# Initial snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Food list (each food has a position, weight, and timer)
foods = []

# Default direction of movement
direction = 'RIGHT'
change_to = direction

# Initial score and level
score = 0
level = 1


# Function to generate new food
# Each food has a weight (points it gives) and a timer before disappearing
def generate_food():
    food_x = random.randrange(1, (window_x // 10)) * 10
    food_y = random.randrange(1, (window_y // 10)) * 10
    weight = random.choice([10, 20, 30])  # Different weight foods
    timer = random.randint(5, 10)  # Food disappears after 5-10 seconds
    foods.append({'position': [food_x, food_y], 'weight': weight, 'timer': time.time() + timer})


# Display score and level
def show_info():
    font = pygame.font.SysFont('times new roman', 25)
    score_surface = font.render(f'Score: {score}  Level: {level}', True, blue)
    game_window.blit(score_surface, (10, 10))


# Game over function
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    message = font.render(f'Game Over! Your Score: {score}', True, red)
    game_window.blit(message, (window_x // 4, window_y // 3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# Initial food generation
generate_food()


def update_food():
    global foods
    current_time = time.time()
    foods = [food for food in foods if food['timer'] > current_time]  # Remove expired food
    if len(foods) < 3:  # Keep at least 3 foods on screen
        generate_food()


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Move in the changed direction
    direction = change_to
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing
    snake_body.insert(0, list(snake_position))
    eaten_food = None
    for food in foods:
        if snake_position == food['position']:
            score += food['weight']  # Add score based on food weight
            eaten_food = food

            # Increase level every 50 points
            if score % 50 == 0:
                level += 1
                snake_speed += 2  # Increase speed
            break

    if eaten_food:
        foods.remove(eaten_food)  # Remove eaten food
    else:
        snake_body.pop()

    # Update food list
    update_food()

    # Fill background and draw snake & food
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    for food in foods:
        color = white if food['weight'] == 10 else red if food['weight'] == 20 else blue
        pygame.draw.rect(game_window, color, pygame.Rect(food['position'][0], food['position'][1], 10, 10))

    # Check for collisions with walls
    if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()

    # Check for collisions with itself
    if snake_position in snake_body[1:]:
        game_over()

    # Display score and level
    show_info()

    # Update screen
    pygame.display.update()

    # Control game speed
    fps.tick(snake_speed)
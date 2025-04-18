import pygame
import time
import random

def start_game(user_id, level, conn, cur):
    score = 0
    snake_speed = 10 + (level - 1) * 2

    window_x = 1000
    window_y = 500

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    pygame.init()
    pygame.display.set_caption('Snake Game with Levels & Timed Food')
    game_window = pygame.display.set_mode((window_x, window_y))
    fps = pygame.time.Clock()

    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    foods = []
    direction = 'RIGHT'
    change_to = direction

    def generate_food():
        food_x = random.randrange(1, (window_x // 10)) * 10
        food_y = random.randrange(1, (window_y // 10)) * 10
        weight = random.choice([10, 20, 30])
        timer = random.randint(5, 10)
        foods.append({'position': [food_x, food_y], 'weight': weight, 'timer': time.time() + timer})

    def show_info():
        font = pygame.font.SysFont('times new roman', 25)
        score_surface = font.render(f'Score: {score}  Level: {level}', True, blue)
        game_window.blit(score_surface, (10, 10))

    def game_over():
        font = pygame.font.SysFont('times new roman', 50)
        message = font.render(f'Game Over! Your Score: {score}', True, red)
        game_window.blit(message, (window_x // 4, window_y // 3))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    def update_food():
        nonlocal foods
        current_time = time.time()
        foods = [food for food in foods if food['timer'] > current_time]
        if len(foods) < 3:
            generate_food()

    def save_score(user_id, level, score, conn, cur):
        cur.execute("""
            INSERT INTO user_score (user_id, level, score)
            VALUES (%s, %s, %s)
        """, (user_id, level, score))
        conn.commit()

    generate_food()

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
                if event.key == pygame.K_p:
                    save_score(user_id, level, score, conn, cur)
                    paused = True
                    font = pygame.font.SysFont('times new roman', 40)
                    pause_text = font.render('Paused. Press P to resume.', True, white)
                    game_window.blit(pause_text, (window_x // 3, window_y // 2))
                    pygame.display.flip()

                    while paused:
                        for pause_event in pygame.event.get():
                            if pause_event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if pause_event.type == pygame.KEYDOWN:
                                if pause_event.key == pygame.K_p:
                                    paused = False
                        time.sleep(0.1)

        direction = change_to
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        eaten_food = None
        for food in foods:
            if snake_position == food['position']:
                score += food['weight']
                eaten_food = food
                if score % 50 == 0:
                    level += 1
                    snake_speed += 2
                break

        if eaten_food:
            foods.remove(eaten_food)
        else:
            snake_body.pop()

        update_food()
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        for food in foods:
            color = white if food['weight'] == 10 else red if food['weight'] == 20 else blue
            pygame.draw.rect(game_window, color, pygame.Rect(food['position'][0], food['position'][1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
            game_over()
        if snake_position in snake_body[1:]:
            game_over()

        show_info()
        pygame.display.update()
        fps.tick(snake_speed)
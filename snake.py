import pygame
import random

def main():
    # pygame setup
    pygame.init()

    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    score=0
    screen.fill("black")
    snake = pygame.draw.rect(screen, "green", (360, 360, 20, 20), 0)
    food = pygame.draw.circle(screen, "orange", (random.randint(0,720), random.randint(0,720)), 4)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # wipe last frame
        screen.fill("black")

        food = pygame.draw.circle(screen, "orange", (food.centerx, food.centery), 4)
        snake = pygame.draw.rect(screen, "green", (snake.left, snake.top, snake.width, snake.height), 0)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            snake.move_ip(-dt * 300, 0)
        elif keys[pygame.K_d]:
            snake.move_ip(dt * 300, 0)
        elif keys[pygame.K_w]:
            snake.move_ip(0, -dt * 300)
        elif keys[pygame.K_s]:
            snake.move_ip(0, dt * 300)

        edgeCollision(snake.left, snake.top, snake.width)
        foodCollision(snake, food, score)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

def edgeCollision(x, y, width):
    if (x > 720-width) or (x < 0) or (y > 720-width) or (y < 0):
        print("Collision with edge. Fail.")
        main()

#TODO fix food spawn
def foodCollision(snake, food, score):
    if snake.colliderect(food):
        food.move_ip(random.randint(0,100), random.randint(0,100))
        score += 100






main()

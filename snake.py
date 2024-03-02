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
    foodX = random.randint(0,720)
    foodY = random.randint(0,720)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # wipe last frame
        screen.fill("black")

        food = pygame.draw.circle(screen, "orange", (foodX, foodY), 4)
        snake = pygame.draw.rect(screen, "green", (snake.left, snake.top, snake.width, snake.height), 0)
        
        keys = pygame.key.get_pressed()
        #if (sum(keys) > 1):
        #    print(sum(keys))
        #    snake.move_ip(0, 0)
        if keys[pygame.K_w]:
            snake.move_ip(0, -dt*300)
        elif keys[pygame.K_s]:
            snake.move_ip(0, dt*300)
        elif keys[pygame.K_a]:
            snake.move_ip(-dt*300, 0)
        elif keys[pygame.K_d]:
            snake.move_ip(dt*300, 0)

        edgeCollision(snake.left, snake.top, snake.width)
        #foodCollision(screen)

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


main()
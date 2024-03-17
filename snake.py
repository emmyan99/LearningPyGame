import pygame
import random

#TODO: SNAP SNAKE TO GRID 
#TODO: FIX FOOD PLACEMENT ON GRID
#TODO: INCREMENT SIZE OF SNAKE
#TODO: FIX MOVEMENT OF LARGER SNAKE
#TODO: COLLISION WITH SELF 
#TODO: FIX SNAKE AUTOMATIC MOVEMENT
#TODO: LEADERBOARD

def main():
    # pygame setup
    pygame.init()

    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    score = 0
    screen.fill("black")
    snake = pygame.draw.rect(screen, "green", (360, 360, 30, 30), 0)
    food = pygame.draw.circle(screen, "orange", (random.randint(0,720), random.randint(0,720)), 4)
    moving = False
    #speed = 1
    lastDir = (0,0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # wipe last frame
        screen.fill("black")

        food = pygame.draw.circle(screen, "orange", (food.centerx, food.centery), 4)
        snake = pygame.draw.rect(screen, "green", (snake.left, snake.top, snake.width, snake.height), 0)
        
        keys = pygame.key.get_pressed()
        if any(keys) == True:
            moving = True

        if moving == True:
            snake, lastDir = snakeMovement(keys, snake, lastDir)
        
        edgeCollision(snake.left, snake.right, snake.top, snake.bottom)
        score, snake = foodCollision(snake, food, score, screen)
        #print(type(snake))
        drawGrid(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        #TODO FIX SCORE VIEW
        # show current score in title
        scoreMsg = "Current score: " + str(score)
        pygame.display.set_caption(scoreMsg)

    pygame.quit()

def edgeCollision(left, right, top, bottom):
    if (left < 0) or (top < 0) or (right > 720) or (bottom > 720):
        print("Collision with edge. Fail.")
        main()

def foodCollision(snake, food, score, screen):
    if snake.colliderect(food):
        foodSpawn(food)
        snake = snakeGrowth(snake, screen)
        score += 100
    return score, snake 

def foodSpawn(food):
    food.move_ip(random.randint(-(food.centerx), 720-(food.centerx)), random.randint(-(food.centery), 720-(food.centery)))

def snakeGrowth(snake, screen):
    tail = pygame.draw.rect(screen, "green", ((snake.left-snake.width), (snake.top+snake.height), snake.width, snake.height), 0)
    snake = snake.union(tail)

def drawGrid(screen):
    for i in range(0, 720, 30):
        pygame.draw.line(screen, (100, 100, 100), (0, i), (720, i))
        pygame.draw.line(screen, (100, 100, 100), (i, 0), (i, 720))
    pygame.display.update()    

def snakeMovement(keys, snake, lastDir):
    #TODO FIX KEY PRIORITY
    dx, dy = 0, 0
    if keys[pygame.K_a]:
        dx -= 2
    elif keys[pygame.K_d]:
        dx += 2
    elif keys[pygame.K_w]:
        dy -= 2
    elif keys[pygame.K_s]: 
        dy += 2
    else:
        (dx,dy) = lastDir
    snake.move_ip(dx, dy)
    return snake, (dx, dy)


main()

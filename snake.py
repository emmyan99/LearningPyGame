import pygame
import random

#TODO: INCREMENT SIZE OF SNAKE, REMOVE UNION AND USE SEVERAL RECTANGLES
#TODO: FIX MOVEMENT OF LARGER SNAKE
#TODO: COLLISION WITH SELF 
#TODO: FIX SNAKE AUTOMATIC MOVEMENT
#TODO: LEADERBOARD

def main():
    # pygame setup
    pygame.init()

    screen = pygame.display.set_mode((720, 720))
    running = True
    score = 0
    screen.fill("black")
    snake = pygame.draw.rect(screen, "green", (360, 360, 30, 30), 0)
    foodX = 15+(30*(random.randint(0,23)))
    foodY = 15+(30*(random.randint(0,23)))
    food = pygame.draw.circle(screen, "orange", (foodX, foodY), 6)
    moving = False
    lastDir = (0,0)
    iterationCounter = 0
    EASY = 60
    MEDIUM = 40
    HARD = 20
    difficulty = EASY

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        iterationCounter +=1

        # wipe last frame
        screen.fill("black")

        food = pygame.draw.circle(screen, "orange", (food.centerx, food.centery), 14)
        snake = pygame.draw.rect(screen, "green", (snake.left, snake.top, snake.width, snake.height), 0)
        
        keys = pygame.key.get_pressed()
        moving = True

        if moving == True:
            if iterationCounter % difficulty == 0:
                snake, lastDir = snakeMovement(keys, snake, lastDir)
        
        edgeCollision(snake.left, snake.right, snake.top, snake.bottom)
        score, snake = foodCollision(snake, food, score, screen)
        drawGrid(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        #TODO FIX SCORE VIEW
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
        snake = snakeGrowth(snake, screen, food)
        score += 100
    return score, snake 

def foodSpawn(food):
    foodX = 15+(30*(random.randint(0,23)))
    foodY = 15+(30*(random.randint(0,23)))
    food.move_ip(foodX, foodY)

#TO BE CHANGED
#Add new rect at end of snake, somehow make them move together
def snakeGrowth(snake, screen, food):
    tail = pygame.draw.rect(screen, "green", (food.centerx-60, food.centery-60, 30, 30), 0)
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
        dx -= 30
    elif keys[pygame.K_d]:
        dx += 30
    elif keys[pygame.K_w]:
        dy -= 30
    elif keys[pygame.K_s]: 
        dy += 30
    else:
        (dx,dy) = lastDir
    snake.move_ip(dx, dy)
    return snake, (dx, dy)


main()

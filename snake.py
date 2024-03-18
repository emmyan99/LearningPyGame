import pygame
import random

#TODO: ADD TAIL TO TAIL, recursive? 
#TODO: MOVEMENT OF LARGER SNAKE, tail must stay behind head
#TODO: INDEPENDENT MOVEMENT OF BODY
#TODO: COLLISION WITH SELF 
#TODO: FIX SNAKE AUTOMATIC MOVEMENT
#TODO: LEADERBOARD

def main():
    # pygame setup
    pygame.init()
    SCREEN_WIDTH = 720
    SCREEN_HEIGHT = 720
    GRID_SIZE = 30
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    score = 0
    screen.fill("black")
    snake = pygame.draw.rect(screen, "green", (SCREEN_WIDTH/2, SCREEN_WIDTH/2, GRID_SIZE, GRID_SIZE), 0)
    foodX = GRID_SIZE//2 + (GRID_SIZE * (random.randint(0, SCREEN_WIDTH//GRID_SIZE-1)))
    foodY = GRID_SIZE//2 + (GRID_SIZE * (random.randint(0, SCREEN_HEIGHT//GRID_SIZE-1)))
    food = pygame.draw.circle(screen, "orange", (foodX, foodY), 6)
    lastDir = (0,0)
    iterationCounter = 0
    snakeSize = 1
    tailPosition = [] # list of tail rect positions
    tails = [] #list of tail rects
    EASY = 200
    MEDIUM = 80
    HARD = 40
    difficulty = EASY

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        iterationCounter +=1

        # wipe last frame
        screen.fill("black")

        food = pygame.draw.circle(screen, "orange", (food.centerx, food.centery), 14)
        snake = pygame.draw.rect(screen, "green", (snake.left, snake.top, snake.width, snake.height), 0)
        if snakeSize > 1:
            for tail in tails: 
                tail = pygame.draw.rect(screen, "green", (tail.left, tail.top, 30, 30), 0)

        if iterationCounter % difficulty == 0:
            snake.move_ip(lastDir)
            if snakeSize > 1:
                tails[0].move_ip(lastDir)
                print("tail x ", tails[0].x)
                print("snake x", snake.x)
            #for i in range(len(tails)):
                #tails[i].move_ip(lastDir)
                
        snake, lastDir = changeDirection(keys, snake, lastDir, GRID_SIZE)
        
        edgeCollision(snake.left, snake.right, snake.top, snake.bottom)
        score, snakeSize, tailPosition, tails = foodCollision(snake, screen, food, score, snakeSize, lastDir, GRID_SIZE, tailPosition, tails)

        drawGrid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
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

def foodSpawn(food):
    food.centerx = 15+(30*(random.randint(0,23)))
    food.centery = 15+(30*(random.randint(0,23)))

def foodCollision(snake, screen, food, score, snakeSize, lastDir, GRID_SIZE, tailPosition, tails):
    if snake.colliderect(food):
        foodSpawn(food)
        score += 10
        snakeSize += 1
        tailPosition = snakeGrowth(snake, lastDir, snakeSize, tailPosition, GRID_SIZE)
        tails = updateTails(tailPosition, screen, tails)
    return score, snakeSize, tailPosition, tails

def updateTails(tailPosition, screen, tails):
    for position in tailPosition:
        newTail = pygame.draw.rect(screen, "green", (position[0], position[1], 30, 30), 0)
        tails.append(newTail)
        return tails

def snakeGrowth(snake, lastDir, snakeSize, tailPosition, GRID_SIZE):
    (tailX, tailY) = tailSpawn(lastDir, snake, GRID_SIZE, snakeSize)
    tailPosition.append((tailX, tailY))
    print(tailPosition)
    return tailPosition

def tailSpawn(lastDir, snake, GRID_SIZE, snakeSize):
    dirX = lastDir[0]
    dirY = lastDir[1]
    if dirX == 0:
        if dirY > 0:
            (x, y) = (snake.x, snake.y - GRID_SIZE/2*snakeSize)
        else:
            (x, y) = (snake.x, snake.y + GRID_SIZE/2*snakeSize)
    else:
        if dirX > 0:
            (x, y) = (snake.x - GRID_SIZE/2*snakeSize, snake.y)
        else:
            (x, y) = (snake.x + GRID_SIZE/2*snakeSize, snake.y)
    return (x, y)

def drawGrid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE):
    for i in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (100, 100, 100), (0, i), (SCREEN_WIDTH, i))
        pygame.draw.line(screen, (100, 100, 100), (i, 0), (i, SCREEN_HEIGHT))
    pygame.display.update()    

def changeDirection(keys, snake, lastDir, GRID_SIZE):
    dx, dy = 0, 0
    if keys[pygame.K_a]:
        dx -= GRID_SIZE
    elif keys[pygame.K_d]:
        dx += GRID_SIZE
    elif keys[pygame.K_w]:
        dy -= GRID_SIZE
    elif keys[pygame.K_s]: 
        dy += GRID_SIZE
    else:
        (dx,dy) = lastDir
    return snake, (dx, dy)


main()

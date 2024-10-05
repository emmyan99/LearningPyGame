# Example file showing a circle moving on screen
import pygame
import sys
import random

#TODO: more words and text wrapping
#TODO: wpm count
#TODO: colour each char once pressed instead of deleting off screen


# pygame setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
#dt = 0

#font for user typed text
base_font = pygame.font.Font(None, 32) 
user_text = '' 

input_rect = pygame.Rect(50, 100, 500, 250) 

color_active = pygame.Color('gray90')
color_passive = pygame.Color('gray95') 
color = color_passive 
  
with open('randomwords.txt') as file:
    allwords = (file.read()).split() #allwords contains a list of words

active = False
indexCounter = 0
indexes = []
running = True
pickwords = True
while running:

    # pick 10 random words from allwords
    while pickwords:
        words = random.sample(allwords, k=2)
        pickwords = False
        words = ' '.join(words)
        wordsToDisplay = words
        print(words)



    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() 

        # if user clicks on input box, the colour active should give feedback, start timer on this click? 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        
        # if input box selected
        if active:
            # if key pressed
                if event.type == pygame.KEYDOWN:

                    if pygame.key.name(event.key) == words[0]:
                        words = words[1:]
                        print("correct")
                        indexes.append(indexCounter)
                        indexCounter += 1
                        print(indexes)
                    elif " " == words[0]:
                        if event.key == pygame.K_SPACE:
                            words = words[1:]
                            print("correct")
                            indexCounter += 1
                        else:
                            print("wrong key, spacebar expected")
                    else:
                        print("wrong key", pygame.key.name(event.key), words[0])

                    
                    
                    #user_text += event.unicode



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("White")

    # decides colour once input box is clicked 
    if active:
        color = color_active
    else:
        color = color_passive

    # draw input rectangle 
    pygame.draw.rect(screen, color, input_rect) 

    x_position = input_rect.x+5
    y_position = input_rect.y+5

    for i, char in enumerate(wordsToDisplay):
        if not i in indexes:
            text_surface = base_font.render(char, True, ("Black"))
        else:
            text_surface = base_font.render(char, True, ("Red")) 


        # render at position stated in arguments 
        screen.blit(text_surface, (x_position, y_position)) 
        x_position += text_surface.get_width()

      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    #input_rect.w = max(100, text_surface.get_width()+10) 


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60)

pygame.quit()
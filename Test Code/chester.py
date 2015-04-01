__author__ = 'John Choo'
import pygame
pygame.init()
import time
import random

display_width = 1000
display_height = 900

black = (0, 0, 0)
white = (255, 255, 255)
grey = (102, 102, 102)
whiteGrey = (204, 204, 204)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rocky Race')
clock = pygame.time.Clock()

def carImage (carx, cary, carw, carh, color):
    pygame.draw.rect(gameDisplay, black, [500, 700, 200, 200])

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, white)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def roadlines(roadlinesx, roadlinesy, roadlinesw, roadlinesh, color):
    pygame.draw.rect(gameDisplay, color, [roadlinesx, roadlinesy, roadlinesw, roadlinesh])

# display car over background(x,y)
def car(x,y):
    gameDisplay.blit(carImage, (x,y))

# rectangle, colour
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# position, font, size
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.4)
    y = (display_height * 0.6)
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

    roadlines_startx = (display_width/2)
    roadlines_starty = -600
    roadlines_speed = 14
    roadlines_width = 30
    roadlines_height = 140

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            # when input is 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        # tally change
        x += x_change

        gameDisplay.fill(grey)

        # (roadlinesx, roadlinesy, roadlinesw, roadlinesh, color)
        roadlines(roadlines_startx, roadlines_starty, roadlines_width, roadlines_height, whiteGrey)
        roadlines_starty += roadlines_speed

        # (thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > (display_width - 164) or x < 0:
            crash()

        # bringing back image
        if roadlines_starty > display_height:
            roadlines_starty = 0 - roadlines_height

        # bringing back image
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            # thing_speed += 0.5
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            if (x > thing_startx and x < thing_startx + thing_width) or (x + thing_width > thing_startx and x + thing_width < thing_startx + thing_width):
                crash()

        pygame.display.update()
        clock.tick(90)

game_loop()
pygame.quit()
quit()
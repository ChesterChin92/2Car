__author__ = 'John Choo'

import pygame
import os

pygame.init()
import time
import random

# original 1080, 1920
display_width = 540
display_height = 960
fpsClock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 254, 255)
grey = (102, 102, 102)
whiteGrey = (204, 204, 204)
backgoundBlue = (35, 52, 122)
dividerBlue = (129, 151, 236)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('2 Car')
clock = pygame.time.Clock()


# carImageRed = pygame.image.load("~Graphics\ed-car.png")
# carImageRed = pygame.image.load(os.path.join(os.path.expanduser("~\PycharmProjects\;2Car"), "Graphics\ed-car.png"))
carImageRed = pygame.image.load(os.path.join(os.path.join(os.curdir, 'Graphics'), "ed-car.png") )
carImageRed = pygame.transform.scale(carImageRed, (54, 96))

# carImageBlue = pygame.image.load("~Graphics\lue_car-v3.png")
carImageBlue = pygame.image.load(os.path.join(os.path.join(os.curdir, 'Graphics'), "lue_car-v3.png") )
carImageBlue = pygame.transform.scale(carImageBlue, (54, 96))

xred = 45
xred_change = 0
yred = 820
xblue = 450
xblue_change = 0
yblue = 820

def background():
    gameDisplay.fill(backgoundBlue)

# line properties
def backgroundline(linex, liney, linew, lineh, color):
    pygame.draw.rect(gameDisplay, color, [linex, liney, linew, lineh])

def circles_hit(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(str(count), True, white)
    gameDisplay.blit(text, (450, 50))

count = 0

def RedCar(xred, yred):
    gameDisplay.blit(carImageRed, (xred, yred))

def BlueCar(xblue, yblue):
    gameDisplay.blit(carImageBlue, (xblue, yblue))

def movement_loop():
    global xred, xred_change
    if xred < 150:
        xred_change += 2

def test():
    print('X Key Pressed')

def movement_loop_test():
    # global xred, xred_change
    # for xred in range(0,150):
    #     print("Current xred Value: %d" %(xred))
    #     xred_change +=1
    #     print("Current xred_change Value: %d" %(xred_change))
    global  xred
    gameDisplay.blit(carImageRed, (xred, yred))
    for xred in range(0,150):
        print("Current xred Value: %d" %(xred))
        xred += 1



def gameloop():
    global xred, xred_change, yred, xblue, xblue_change, yblue

    gameExit = False
    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x and xred <150 :
                    movement_loop_test()
                if event.key == pygame.K_z and xred > 0 :
                    xred -= 10



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z or event.key == pygame.K_x:
                    xred_change = 0
                # elif event.key == pygame.K_c:


        xred += xred_change

        # background
        background()
        backgroundline(135, 0, 8.571, 2000, dividerBlue)
        backgroundline((display_width - 135), 0, 8.571, 2000, dividerBlue)
        backgroundline((display_width/2), 0, 17.142, 2000, dividerBlue)

        #cars
        # RedCar(xred, yred)
        gameDisplay.blit(carImageRed, (xred, yred))
        BlueCar(xblue, yblue)

        pygame.display.update()
        fpsClock.tick(90)
        # clock.tick(90)


gameloop()
pygame.quit()
quit()


__author__ = 'Chester Chin'


# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)



def draw_stick_figure2(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, GREEN, [1 + x, y, 20, 20], 0)




# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

x_speed_2 = 0
y_speed_2 = 0

# Current position
x_coord = 10
y_coord = 10

x_coord_2 = 10
y_coord_2 = 10


# -------- Main Program Loop -----------#
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                 for counter in range(0,10):
                    x_speed = counter
                    x_coord = x_coord - x_speed
                    screen.fill(WHITE)
                    draw_stick_figure(screen, x_coord, y_coord)
                    draw_stick_figure2(screen, x_coord_2, y_coord_2)
                    pygame.display.flip()
                    clock.tick(60)
            elif event.key == pygame.K_RIGHT:
                for counter in range(0,10):
                    x_speed = counter
                    x_coord = x_coord + x_speed
                    screen.fill(WHITE)
                    draw_stick_figure(screen, x_coord, y_coord)
                    pygame.display.flip()
                    clock.tick(60)

            elif event.key == pygame.K_UP:
                for counter in range(0,10):
                    y_speed = counter
                    y_coord = y_coord - y_speed
                    screen.fill(WHITE)
                    draw_stick_figure(screen, x_coord, y_coord)
                    pygame.display.flip()
                    clock.tick(60)
            elif event.key == pygame.K_DOWN:
                for counter in range(0,10):
                    y_speed = counter
                    y_coord = y_coord + y_speed
                    screen.fill(WHITE)
                    draw_stick_figure(screen, x_coord, y_coord)
                    pygame.display.flip()
                    clock.tick(60)
            if event.key == pygame.K_a:
                 for counter in range(0,10):
                    x_speed_2 = counter
                    x_coord_2 = x_coord_2 - x_speed_2
                    screen.fill(WHITE)
                    draw_stick_figure2(screen, x_coord_2, y_coord_2)
                    pygame.display.flip()
                    clock.tick(60)

             # THIS WILL NOT MAKE STUFF BLIP WHILE MOVING
            elif event.key == pygame.K_d:
                for counter in range(0,10):
                    x_speed_2 = counter
                    x_coord_2 = x_coord_2 + x_speed_2
                    screen.fill(WHITE)
                    draw_stick_figure2(screen, x_coord_2, y_coord_2)
                    draw_stick_figure(screen, x_coord, y_coord)
                    pygame.display.flip()
                    clock.tick(60)

            elif event.key == pygame.K_w:
                for counter in range(0,10):
                    y_speed_2 = counter
                    y_coord_2 = y_coord_2 - y_speed_2
                    screen.fill(WHITE)
                    draw_stick_figure2(screen, x_coord_2, y_coord_2)
                    pygame.display.flip()
                    clock.tick(60)
            elif event.key == pygame.K_s:
                for counter in range(0,10):
                    y_speed_2 = counter
                    y_coord_2 = y_coord_2 + y_speed_2
                    screen.fill(WHITE)
                    draw_stick_figure2(screen, x_coord_2, y_coord_2)
                    pygame.display.flip()
                    clock.tick(60)

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed=0
            elif event.key == pygame.K_RIGHT:
                x_speed=0
            elif event.key == pygame.K_UP:
                y_speed=0
            elif event.key == pygame.K_DOWN:
                y_speed=0
            if event.key == pygame.K_a:
                x_speed_2= 0
            elif event.key == pygame.K_d:
                x_speed_2= 0
            elif event.key == pygame.K_w:
                y_speed_2= 0
            elif event.key == pygame.K_s:
                y_speed_2 =0
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # Move the object according to the speed vector.
    # x_coord = x_coord + x_speed
    # y_coord = y_coord + y_speed

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    #screen.fill(WHITE)

    #draw_stick_figure(screen, x_coord, y_coord)
    #draw_stick_figure2(screen, x_coord_2, y_coord_2)
    pygame.display.flip()
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    # pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

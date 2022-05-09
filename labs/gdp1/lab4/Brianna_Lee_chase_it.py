# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 225)


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, WHITE, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, GREEN, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [1 + x, 17 + y], 2)


# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Lab 4 - Brianna Lee")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# See the mouse cursor
pygame.mouse.set_visible(1)

# code to chase the mouse
x_stick = 10
y_stick = 10

X_SPEED = 3
Y_SPEED = 3

# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # Call draw stick figure function
    pos = pygame.mouse.get_pos()
    x_mouse = pos[0]
    y_mouse = pos[1]

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    #code to chase the mouse
    sx = x_mouse - x_stick
    sy = y_mouse - y_stick

    theta = math.atan2(sx,sy)

    dx = X_SPEED * math.sin(theta)
    dy = Y_SPEED * math.cos(theta)

    x_stick += dx
    y_stick += dy

    #snapping the figure
    if (x_stick - x_mouse <= X_SPEED) and (y_stick - y_mouse <= Y_SPEED):
        x_stick = x_mouse
        y_stick = y_mouse

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    screen.fill(BLACK)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("You're IT!", True, WHITE)

    #prints the text if the figure is exactly where the mouse is
    if (x_stick == x_mouse) and (y_stick == y_mouse):
        screen.blit(text, [250, 250])


    draw_stick_figure(screen, x_stick, y_stick)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

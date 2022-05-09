"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# rectangle class
class Rectangle():
    # class attributes
    def __init__(self):
        self.xPosition = 0
        self.yPosition = 0
        self.height = 0
        self.width = 0
        self.xChange = 0
        self.yChange = 0
        self.color = (0, 0, 255)

    # drawing the rectangle
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.xPosition, self.yPosition, self.height, self.width])

    # moving the rectangles
    def move(self):
        self.xPosition += self.xChange
        self.yPosition += self.yChange

# ellipse class
class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.xPosition, self.yPosition, self.height, self.width])

myList = []

for i in range(1000):
    # created instance for rectangle
    myObject = Rectangle()
    myObject.height = random.randrange(20, 70)
    myObject.width = random.randrange(20, 70)
    myObject.xPosition = random.randrange(0, 700)
    myObject.yPosition = random.randrange(0, 500)
    myObject.xChange = random.randrange(-3,3)
    myObject.yChange = random.randrange(-3, 3)

    # random colors
    myObject.color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

    # adding object to list
    myList.append(myObject)

for i in range(1000):
    # created instance for ellipse
    myObject = Ellipse()
    myObject.height = random.randrange(20, 70)
    myObject.width = random.randrange(20, 70)
    myObject.xPosition = random.randrange(0, 700)
    myObject.yPosition = random.randrange(0, 500)
    myObject.xChange = random.randrange(-3,3)
    myObject.yChange = random.randrange(-3, 3)

    # random colors
    myObject.color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

    # adding object to list
    myList.append(myObject)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Lab 5 - Brianna Lee")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    for i in range(len(myList)):
        myList[i].draw()
        myList[i].move()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

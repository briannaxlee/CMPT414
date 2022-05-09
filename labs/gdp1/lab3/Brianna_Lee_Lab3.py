"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
TEAL     = (   0, 128, 128)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Brianna Lee Lab 3")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    screen.fill(WHITE)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render("Brianna Lee's Lab 3", True, BLACK)
    
    screen.blit(text, [400,400])

    #house

    #chimney
    pygame.draw.rect(screen, BLACK, [60,200,20,50], 0)

    #roof
    pygame.draw.polygon(screen, BLACK, [[150,150], [50,250], [250,250]], 5)
    pygame.draw.polygon(screen, WHITE, [[150,150], [50,250], [250,250]], 0)

    #main house
    pygame.draw.rect(screen, BLUE, [50,250,200,200],0)

    #windows
    x = 70
    for i in range(4):
        pygame.draw.rect(screen, BLACK, [x, 300, 10, 30], 0)
        x = x + 50

    #door
    pygame.draw.rect(screen, TEAL, [140, 400, 20, 50], 0)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()


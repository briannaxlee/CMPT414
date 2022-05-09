"""
Brianna Lee
Version 1.01
The code here creates the game Space Invaders screen and controls different aspects of the game. For example,
it creates text at the beginning of the game and at the end of the game to indicate that the game is starting,
the player has either won or lost the game. It also creates the classes of the spaceship, spaceship bullets,
the enemies, their bullets, and explosions. It also creates the key movements of the spaceship and the formation
of the aliens.
The player moves their character, the spaceship, using the left and right arrow key to move side to side. The
space bar is there for the player to shoot their bullets at the opponent. If the player's bullet hits the enemy,
the enemy will explode. However, if the player gets hit by the enemies' bullet, the player will lose a bit of
their health that cannot be revived. In order for the player to win the game, they have to shoot all of the enemies
down before their health depletes from the enemies' bullets.
At this point, things are somewhat are okay. I have to connect main.py and menu.py to one another so that the menu.py
can access the main.py so the player can play the game. I also have to implement background audio so the player can
listen to 8-bit like music while the player is playing the game. Other than that, I also have to work on animating
the enemy sprites while they move side to side. After everything I will modularize the code so there aren't over
hundreds of lines in the main.py.
"""
import sys
import time

import pygame
from pygame import mixer
from pygame.locals import *
import random

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("img/space.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.75)

# define fps
clock = pygame.time.Clock()
fps = 60

screenWidth = 600
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Brianna Lee - Final Project')

# define fonts
font30 = pygame.font.SysFont('Arial', 30)
font40 = pygame.font.SysFont('Arial', 40)

# load sounds
explosionSound = pygame.mixer.Sound("img/explosion.wav")
explosionSound.set_volume(0.05)

explosionSound2 = pygame.mixer.Sound("img/explosion2.wav")
explosionSound2.set_volume(0.05)

laserSound = pygame.mixer.Sound("img/laser.wav")
laserSound.set_volume(0.05)

# define game variables
rows = 5
column = 5
alienCooldown = 1000  # bullet cooldown in milliseconds

# define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# load image
background = pygame.image.load("img/bg.png")


def drawBackground():
    screen.blit(background, (0, 0))


# define function for creating text
def drawText(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# def drawStartScreen():

# create spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # set movement speed
        speed = 8
        # set a cooldown variable
        cooldown = 500  # milliseconds
        game_over = 0

        # get key press
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screenWidth:
            self.rect.x += speed
        if key[pygame.K_q]:
            pygame.quit()

        # record current time
        timeNow = pygame.time.get_ticks()
        # shoot
        if key[pygame.K_SPACE] and timeNow - self.last_shot > cooldown:
            laserSound.play()
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bulletGroup.add(bullet)
            self.last_shot = timeNow

        # update mask
        self.mask = pygame.mask.from_surface(self.image)

        # draw health bar
        pygame.draw.rect(screen, RED, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, GREEN, (
                self.rect.x, (self.rect.bottom + 10),
                int(self.rect.width * (self.health_remaining / self.health_start)),
                15))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosionGroup.add(explosion)
            self.kill()
            game_over = -1
        return game_over


# create Bullets class
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alienGroup, True):
            self.kill()
            explosionSound.play()
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosionGroup.add(explosion)


# create Aliens class
class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/alien" + str(random.randint(1, 5)) + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction


# create Alien Bullets class
class AlienBullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/alien_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 2
        if self.rect.top > screenHeight:
            self.kill()
        if pygame.sprite.spritecollide(self, spaceshipGroup, False, pygame.sprite.collide_mask):
            self.kill()
            explosionSound2.play()
            # reduce spaceship health
            spaceship.health_remaining -= 1
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosionGroup.add(explosion)


# create Explosion class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"img/exp{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            if size == 2:
                img = pygame.transform.scale(img, (40, 40))
            if size == 3:
                img = pygame.transform.scale(img, (160, 160))
            # add the image to the list
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosionSpeed = 3
        # update explosion animation
        self.counter += 1

        if self.counter >= explosionSpeed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # if the animation is complete, delete explosion
        if self.index >= len(self.images) - 1 and self.counter >= explosionSpeed:
            self.kill()


# create sprite groups
spaceshipGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
alienGroup = pygame.sprite.Group()
alienBulletGroup = pygame.sprite.Group()
explosionGroup = pygame.sprite.Group()


def createAliens():
    # generate aliens
    for row in range(rows):
        for item in range(column):
            alien = Aliens(100 + item * 100, 100 + row * 70)
            alienGroup.add(alien)


createAliens()

# create player
spaceship = Spaceship(int(screenWidth / 2), screenHeight - 100, 3)
spaceshipGroup.add(spaceship)


def mainloop():
    # define the game variables
    countdown = 3
    lastCount = pygame.time.get_ticks()
    gameOver = 0  # 0 is nothing, 1 means player has won, -1 means player has lost
    lastAlienShot = pygame.time.get_ticks()

    run = True
    while run:

        clock.tick(fps)

        # draw background
        drawBackground()

        if countdown == 0:
            # create random alien bullets
            # record current time
            timeNow = pygame.time.get_ticks()
            # shoot
            if timeNow - lastAlienShot > alienCooldown and len(alienBulletGroup) < 5 and len(alienGroup) > 0:
                attacking_alien = random.choice(alienGroup.sprites())
                alien_bullet = AlienBullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
                alienBulletGroup.add(alien_bullet)
                lastAlienShot = timeNow

            # check if all the aliens have been killed
            if len(alienGroup) == 0:
                gameOver = 1

            if gameOver == 0:
                # update spaceship
                gameOver = spaceship.update()

                # update sprite groups
                bulletGroup.update()
                alienGroup.update()
                alienBulletGroup.update()
            else:
                if gameOver == -1:
                    drawText('GAME OVER!', font40, WHITE, int(screenWidth / 2 - 110), int(screenHeight / 2))
                if gameOver == 1:
                    drawText('YOU WIN!', font40, WHITE, int(screenWidth / 2 - 100), int(screenHeight / 2))

        if countdown > 0:
            drawText('GET READY!', font40, WHITE, int(screenWidth / 2 - 110), int(screenHeight / 2))
            drawText(str(countdown), font40, WHITE, int(screenWidth / 2 - 10), int(screenHeight / 2 + 40))
            countTimer = pygame.time.get_ticks()
            if countTimer - lastCount > 1000:
                countdown -= 1
                lastCount = countTimer

        # update explosion group
        explosionGroup.update()

        # draw sprite groups
        spaceshipGroup.draw(screen)
        bulletGroup.draw(screen)
        alienGroup.draw(screen)
        alienBulletGroup.draw(screen)
        explosionGroup.draw(screen)

        # event handlers

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


mainloop()
pygame.quit()

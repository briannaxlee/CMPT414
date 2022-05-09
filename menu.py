import pygame
import sys

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Main Menu")
background = pygame.image.load("img/bg.png")
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont("Arial", 20)

pygame.mixer.init()
pygame.mixer.music.load("img/space.wav")
pygame.mixer.music.play(999)


def drawBackground():
    screen.blit(background, (0, 0))


def drawText(text, font, color, surface, x, y):
    textObject = font.render(text, 1, color)
    textRectangle = textObject.get_rect()
    textRectangle.topleft = (x, y)
    surface.blit(textObject, textRectangle)


click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        drawBackground()
        drawText("Main Menu - ESC to QUIT", font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(50, 100, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)
        if button1.collidepoint((mx, my)):
            if click:
                game()
        if button2.collidepoint((mx, my)):
            if click:
                rules()
        pygame.draw.rect(screen, (255, 0, 0), button1)
        drawText("Play Game", font, (255, 255, 255), screen, 60, 110)

        pygame.draw.rect(screen, (255, 0, 0), button2)
        drawText("Rules", font, (255, 255, 255), screen, 60, 210)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        drawBackground()

        drawText("GAME", font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            import main
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def rules():
    running = True
    while running:
        screen.fill((0, 0, 0))
        drawBackground()

        drawText("Rules- ESC to GO BACK", font, (255, 255, 255), screen, 20, 20)

        drawText("HOW TO PLAY", font, (255, 255, 255), screen, 60, 100)
        drawText("Use the LEFT and RIGHT arrow keys to", font, (255, 255, 255), screen, 60, 130)
        drawText("move the spaceship. Press SPACEBAR", font, (255, 255, 255), screen, 60, 160)
        drawText("Player's health can be seen at the bottom", font, (255, 255, 255), screen, 60, 190)
        drawText("of the screen. Hit by three enemy bullets", font, (255, 255, 255), screen, 60, 220)
        drawText("and the player loses. Hit all of the enemies.", font, (255, 255, 255), screen, 60, 250)
        drawText("to win. Hit ESC to QUIT.", font, (255, 255, 255), screen, 60, 280)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()

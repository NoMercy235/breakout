import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

helloWorld = pygame.image.load("PS circle.png")
helloWorldSize = helloWorld.get_size()

sound = pygame.mixer.Sound("Pluralsight.wav")
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.play(0)

clock = pygame.time.Clock()

while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            sound.stop()
            sound.play()

    screen.fill((0, 0, 0))

    x, y = pygame.mouse.get_pos()

    x = windowSize[0] - helloWorldSize[0] if x + helloWorldSize[0] > windowSize[0] else x
    y = windowSize[1] - helloWorldSize[1] if y + helloWorldSize[1] > windowSize[1] else y

    screen.blit(helloWorld, (x, y))

    pygame.display.update()

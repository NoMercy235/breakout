import pygame
import sys

pygame.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Hello World!", 1, (255, 0, 0), (255, 255, 255))
helloWorldSize = helloWorld.get_size()


direction = (1, 1)

clock = pygame.time.Clock()

# The game loop
while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    x, y = pygame.mouse.get_pos()

    x = windowSize[0] - helloWorldSize[0] if x + helloWorldSize[0] > windowSize[0] else x
    y = windowSize[1] - helloWorldSize[1] if y + helloWorldSize[1] > windowSize[1] else y

    screen.blit(helloWorld, (x, y))

    pygame.display.update()

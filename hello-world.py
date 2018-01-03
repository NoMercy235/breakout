import pygame
import sys
import random

pygame.init()

# windowSize = {"height": 800, "width": 600}
windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Hello World!", 1, (255, 0, 0), (255, 255, 255))
helloWorldSize = helloWorld.get_size()

x, y = 0, 0
direction = (1, 1)

clock = pygame.time.Clock()

# The game loop
while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    screen.blit(helloWorld, (x, y))

    x += 5 * direction[0]
    y += 5 * direction[1]

    if x + helloWorldSize[0] > windowSize[0] or x < 0:
        direction = (-1 * direction[0], direction[1])

    if y + helloWorldSize[1] > windowSize[1] or y < 0:
        direction = (direction[0], -1 * direction[1])

    pygame.display.update()

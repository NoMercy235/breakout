import pygame
import sys
import random

pygame.init()

# windowSize = {"height": 800, "width": 600}
windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Hello World!", 1, (255, 0, 0), (255, 255, 255))

x, y = 0, 0

clock = pygame.time.Clock()

# The game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    screen.blit(helloWorld, (x, y))

    x = x + 1 if x < 800 else random.randint(0, 800)
    y = y + 1 if y < 600 else random.randint(0, 600)

    pygame.display.update()

# pygame.
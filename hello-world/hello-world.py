import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

helloWorld = pygame.image.load("./hello-world/PS circle.png")
helloWorldSize = helloWorld.get_size()

sound = pygame.mixer.Sound("./hello-world/Pluralsight.wav")
pygame.mixer.music.load("./hello-world/test.mp3")
pygame.mixer.music.play(0)

clock = pygame.time.Clock()

x, y = 0, 0

while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            sound.stop()
            sound.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    if keys[pygame.K_UP]:
        y -= 5

    screen.fill((0, 0, 0))

    x = windowSize[0] - helloWorldSize[0] if x + helloWorldSize[0] > windowSize[0] else 0 if x < 0 else x
    y = windowSize[1] - helloWorldSize[1] if y + helloWorldSize[1] > windowSize[1] else 0 if y < 0 else y

    screen.blit(helloWorld, (x, y))

    pygame.display.update()

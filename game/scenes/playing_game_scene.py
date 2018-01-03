import pygame
from game.scenes.scene import Scene


class PlayingGameScene(Scene):

    def __init__(self, game):
        super().__init__(game)

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

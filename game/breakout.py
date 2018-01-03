import pygame

from game import *
from game.scenes import *
from game.shared import Constants


class Breakout:

    def __init__(self):
        self._lives = Constants.INITIAL_LIVES
        self._score = 0

        self._level = Level(self)
        self._level.load_level(0)

        self._pad = Pad((0, 0), 0)
        self._balls = [
            Ball((0, 0), 0, self)
        ]

        pygame.init()
        pygame.mixer.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(Constants.TEXTS["CAPTION"])

        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        self._scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighScoreScene(self),
            MenuScene(self),
        )

        self._current_scene = 0

        self._sounds = ()

    def start(self):
        while 1:
            self._clock.tick(Constants.FPS)
            self.screen.fill((0, 0, 0))

            current_scene = self._scenes[self._current_scene]
            current_scene.handle_events(pygame.event.get())
            current_scene.render()

            pygame.display.update()

    def change_scene(self, scene):
        self._current_scene = scene

    def get_level(self):
        return self._level

    def get_score(self):
        return self._score

    def increase_score(self, amount: int):
        self._score += amount

    def get_lives(self):
        return self._lives

    def get_balls(self):
        return self._balls

    def get_pad(self):
        return self._pad

    def play_sound(self, sound):
        pass

    def reduce_lives(self):
        pass

    def increase_lives(self):
        pass

    def reset(self):
        pass


Breakout().start()

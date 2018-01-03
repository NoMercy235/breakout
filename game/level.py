import os
import fileinput
from game.bricks import Brick
from game.shared import pygame, Constants


class Level:

    def __init__(self, game):
        self._game = game
        self._bricks = []
        self._bricks_left = 0
        self._current_level = 0

    def get_bricks(self):
        return self._bricks

    def get_bricks_left(self):
        return self._bricks_left

    def brick_hit(self):
        self._bricks_left -= 1

    def load_level(self, level):
        self._current_level = level
        self._bricks = []

        x, y = 0, 0

        for line in fileinput.input(os.path.join("assets", "levels", "level" + str(level) + ".dat")):
            for current_brick in line:
                brick_image = None
                if current_brick == "1":
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-NORMAL"])
                elif current_brick == "2":
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-SPEED"])
                elif current_brick == "3":
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-LIFE"])

                if brick_image is not None:
                    brick = Brick([x, y], brick_image, self._game)
                    self._bricks.append(brick)
                    self._bricks_left += 1

                x += Constants.BRICK["SIZE"][0]

            x = 0
            y += Constants.BRICK["SIZE"][1]

    def load_next_level(self):
        pass

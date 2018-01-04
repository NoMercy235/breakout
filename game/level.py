import os
import fileinput
import random
from game.bricks import Brick, LifeBrick, SpeedBrick
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
        self._bricks_left = 0

        x, y = 0, 0

        for line in fileinput.input(os.path.join("assets", "levels", "level" + str(level) + ".dat")):
            for current_brick in line:
                brick = None
                if current_brick == "1":
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-NORMAL"])
                    brick = Brick([x, y], brick_image, self._game)
                elif current_brick == "2":
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-SPEED"])
                    brick = SpeedBrick([x, y], brick_image, self._game)
                elif current_brick == "3":
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-LIFE"])
                    brick = LifeBrick([x, y], brick_image, self._game)

                if brick is not None:
                    self._bricks.append(brick)
                    self._bricks_left += 1

                x += Constants.BRICK["SIZE"][0]

            x = 0
            y += Constants.BRICK["SIZE"][1]

    def load_random_level(self):
        self._bricks = []
        self._bricks_left = 0

        x, y = 0, 0

        max_bricks = int(Constants.SCREEN_SIZE[0] / Constants.BRICK["SIZE"][0])
        rows = random.randint(3, 6)

        for row in range(0, rows):
            for brick in range(0, max_bricks):
                brick_type = random.randint(0, 3)
                brick = None
                if brick_type == 1:
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-NORMAL"])
                    brick = Brick([x, y], brick_image, self._game)
                elif brick_type == 2:
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-SPEED"])
                    brick = SpeedBrick([x, y], brick_image, self._game)
                elif brick_type == 3:
                    brick_image = pygame.image.load(Constants.SPRITES["BRICK-LIFE"])
                    brick = LifeBrick([x, y], brick_image, self._game)

                if brick is not None:
                    self._bricks.append(brick)
                    self._bricks_left += 1

                x += Constants.BRICK["SIZE"][0]

            x = 0
            y += Constants.BRICK["SIZE"][1]

    def load_next_level(self):
        self._current_level += 1
        file_name = os.path.join("assets", "levels", "level" + str(self._current_level) + ".dat")

        if not os.path.exists(file_name):
            self.load_random_level()
        else:
            self.load_level(self._current_level)

from game.shared import *


class Ball(GameObject):

    def __init__(self, position, sprite, game):
        self._game = game
        self._speed = Constants.BALL["SPEED"]
        self._increment = [2, 2]
        self._direction = [1, 1]
        self._moving = False
        super().__init__(position, Constants.BALL["SIZE"], sprite)

    def set_speed(self, speed):
        self._speed = speed

    def reset_speed(self):
        self._speed = Constants.BALL["SPEED"]

    def get_speed(self):
        return self._speed

    def is_moving(self):
        return self._moving

    def set_moving(self, moving):
        self._moving = moving
        self.reset_speed()

    def change_direction(self, game_object):
        pass

    def update_position(self):
        self.set_position(pygame.mouse.get_pos())

    def is_dead(self):
        pass

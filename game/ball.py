from game.shared import GameObject, Constants, pygame


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

    def set_is_moving(self, moving):
        self._moving = moving
        self.reset_speed()

    def change_direction(self, game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        if object_position[1] < position[1] < object_position[1] + object_size[1] and \
                object_position[0] < position[0] < object_position[0] + object_size[0]:
            self.set_position((position[0], object_position[1] + object_size[1]))
            self._direction[1] *= -1

        elif object_position[1] < position[1] + size[1] < object_position[1] + object_size[1] and \
                object_position[0] < position[0] < object_position[0] + object_size[0]:
            self.set_position((position[0], object_position[1] - object_size[1]))
            self._direction[1] *= -1

        elif object_position[0] < position[0] + size[0] < object_position[0] + object_size[0]:
            self.set_position((object_position[0] - size[0], position[1]))
            self._direction[0] *= -1

        else:
            self.set_position((object_position[0] + object_size[0], position[1]))
            self._direction[0] *= -1
            self._direction[1] *= -1

    def update_position(self):
        if not self.is_moving():
            pad_position = self._game.get_pad().get_position()
            self.set_position((
                pad_position[0] + (Constants.PAD_SIZE[0] / 2),
                Constants.SCREEN_SIZE[1] - Constants.PAD_SIZE[1] - Constants.SPACE_BELOW_PAD - Constants.BALL["SIZE"][1]
            ))
            return

        position = self.get_position()
        size = self.get_size()

        new_position = [
            position[0] + (self._increment[0] * self._speed) * self._direction[0],
            position[1] + (self._increment[1] * self._speed) * self._direction[1]
        ]

        if new_position[0] + size[0] >= Constants.SCREEN_SIZE[0]:
            self._direction[0] *= -1
            new_position = [Constants.SCREEN_SIZE[0] - size[0], new_position[1]]

        if new_position[0] <= 0:
            self._direction[0] *= -1
            new_position = [0, new_position[1]]

        if new_position[1] + size[1] >= Constants.SCREEN_SIZE[1]:
            self._direction[1] *= -1
            new_position = [new_position[0], Constants.SCREEN_SIZE[1] - size[1]]

        if new_position[1] <= 0:
            self._direction[1] *= -1
            new_position = [new_position[0], 0]

        self.set_position(new_position)

    def is_dead(self):
        position = self.get_position()
        size = self.get_size()
        if position[1] + size[1] >= Constants.SCREEN_SIZE[1]:
            return True
        return False

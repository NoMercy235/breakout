from game.shared import *


class Pad(GameObject):

    def __init__(self, position, sprite):
        super().__init__(position, Constants.PAD_SIZE, sprite)

    def set_position(self, position):
        new_position = [position[0], position[1]]
        size = self.get_size()

        if new_position[0] + size[0] > Constants.SCREEN_SIZE[0]:
            new_position[0] = Constants.SCREEN_SIZE[0] - size[0]

        return super().set_position(new_position)
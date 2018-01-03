from game.shared import *


class Pad(GameObject):

    def __init__(self, position, sprite):
        super().__init__(position, Constants.PAD_SIZE, sprite)

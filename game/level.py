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
        pass

    def load_next_level(self):
        pass

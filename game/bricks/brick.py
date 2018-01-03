from game.shared import GameObject
from game.shared import Constants


class Brick(GameObject):

    def __init__(self, position, sprite, game):
        self._game = game
        self._hp = Constants.BRICK["HP"]
        self._lives = Constants.BRICK["LIVES"]
        super().__init__(position, Constants.BRICK["SIZE"], sprite)

    def get_game(self):
        return self._game

    def is_destroyed(self):
        return self._lives <= 0

    def get_hp(self):
        return self._hp

    def hit(self):
        self._lives -= 1

    def get_hit_sound(self):
        pass
from game.bricks import Brick
from game.shared import Constants


class LifeBrick(Brick):

    def __init__(self, position, sprite, game):
        super().__init__(position, sprite, game)

    def hit(self):
        game = self.get_game()
        game.increase_lives()
        super().hit()

    def get_hit_sound(self):
        return Constants.SOUNDS["HIT_BRICK_LIFE"][0]

from game.bricks import Brick


class LifeBrick(Brick):

    def __init__(self, position, sprite, game):
        super().__init__(position, sprite, game)

    def hit(self):
        game = self.get_game()
        game.increase_lives()
        super().hit()

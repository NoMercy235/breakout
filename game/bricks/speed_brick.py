from game.bricks import Brick
from game.shared import Constants


class SpeedBrick(Brick):

    def __init__(self, position, sprite, game):
        super().__init__(position, sprite, game)

    def hit(self):
        game = self.get_game()
        for ball in game.get_balls():
            if ball.get_speed() < Constants.BALL["MAX_SPEED"]:
                ball.set_speed(ball.get_speed() + Constants.BALL["SPEED_INCREASE"])
        super().hit()

    def get_hit_sound(self):
        return Constants.SOUNDS["HIT_BRICK_SPEED"][0]

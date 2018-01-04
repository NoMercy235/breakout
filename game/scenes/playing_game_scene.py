from game.scenes.scene import Scene
from game.shared import Constants, pygame


class PlayingGameScene(Scene):

    def __init__(self, game):
        super().__init__(game)

    def render(self):
        super().render()
        game = self.get_game()

        if game.get_lives() <= 0:
            game.play_sound(Constants.SOUNDS["GAME_OVER"][0])
            game.change_scene(Constants.SCENES["GAME_OVER"])

        pad = game.get_pad()
        pad.set_position((pygame.mouse.get_pos()[0], pad.get_position()[1]))
        game.screen.blit(pad.get_sprite(), pad.get_position())

        balls = game.get_balls()
        for ball in balls:
            # If you want balls to bounce on each other. Might remove.
            for other_ball in balls:
                if ball != other_ball and ball.intersects(other_ball):
                    ball.change_direction(other_ball)

            for brick in game.get_level().get_bricks():
                if not brick.is_destroyed() and ball.is_moving() and ball.intersects(brick):
                    brick.hit()
                    game.play_sound(brick.get_hit_sound())
                    game.increase_score(brick.get_hp())
                    ball.change_direction(brick)
                    break

            if ball.intersects(pad):
                game.play_sound(Constants.SOUNDS["HIT_PAD"][0])
                ball.change_direction(pad)

            ball.update_position()
            game.screen.blit(ball.get_sprite(), ball.get_position())

            if ball.is_dead():
                ball.set_is_moving(False)
                if len(game.get_balls()) == 1:
                    game.reduce_lives()

        for brick in game.get_level().get_bricks():
            if not brick.is_destroyed():
                game.screen.blit(brick.get_sprite(), brick.get_position())

        self.clear_text()

        self.add_text("Score: " + str(game.get_score()), x=PlayingGameScene.compute_x_offset(game),
                      y=Constants.SCREEN_SIZE[1] - 30, size=30)
        self.add_text("Lives: " + str(game.get_lives()), x=0, y=Constants.SCREEN_SIZE[1] - 30, size=30)

    @staticmethod
    def compute_x_offset(game):
        score_digits = 0
        score = game.get_score()
        while score > 0:
            score_digits += 1
            score = int(score / 10)
        return Constants.SCREEN_SIZE[0] - 100 - (10 * score_digits)

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.get_game().get_balls():
                    ball.set_is_moving(True)

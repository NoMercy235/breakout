from game.scenes.scene import Scene
from game.shared import pygame


class PlayingGameScene(Scene):

    def __init__(self, game):
        super().__init__(game)

    def render(self):
        super().render()
        game = self.get_game()

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
                if not brick.is_destroyed() and ball.intersects(brick):
                    brick.hit()
                    ball.change_direction(brick)
                    break

            if ball.intersects(pad):
                ball.change_direction(pad)

            ball.update_position()
            game.screen.blit(ball.get_sprite(), ball.get_position())

        for brick in game.get_level().get_bricks():
            if not brick.is_destroyed():
                game.screen.blit(brick.get_sprite(), brick.get_position())

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.get_game().get_balls():
                    ball.set_is_moving(True)

from game.scenes.scene import Scene
from game.shared import pygame


class PlayingGameScene(Scene):

    def __init__(self, game):
        super().__init__(game)

    def render(self):
        super().render()
        game = self.get_game()

        for ball in game.get_balls():
            for brick in game.get_level().get_bricks():
                if ball.intersects(brick):
                    brick.hit()
                    ball.change_direction(brick)
                    break

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

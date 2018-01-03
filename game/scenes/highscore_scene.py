from game.scenes.scene import Scene
from game.shared import Constants, pygame
from game import HighScore


class HighScoreScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self._high_score_sprite = pygame.image.load(Constants.SPRITES["HIGH_SCORE"])

    def render(self):
        self.get_game().screen.blit(self._high_score_sprite, (50, 50))

        self.clear_text()

        high_score = HighScore()

        x = 350
        y = 100
        for score in high_score.get_scores():
            self.add_text(score[0], x, y, size=30)
            self.add_text(str(score[1]), x + 200, y, size=30)

            y += 30

        self.add_text("Press F1 to restart the game.", x, y + 60, size=30)

        super().render()

    def handle_events(self, events):
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.get_game().reset()
                    self.get_game().change_scene(Constants.SCENES["PLAYING"])

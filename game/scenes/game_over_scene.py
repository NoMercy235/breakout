from game.scenes.scene import Scene
from game.shared import Constants, pygame
from game import HighScore


class GameOverScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self._player_name = ""
        self._high_score_sprite = pygame.image.load(Constants.SPRITES["HIGH_SCORE"])

    def render(self):
        self.get_game().screen.blit(self._high_score_sprite, (50, 50))

        self.clear_text()
        self.add_text("Your name: ", 300, 200, size=30)
        self.add_text(self._player_name, 420, 200, size=30)

        super().render()

    def handle_events(self, events):
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.get_game().reset()
                    self.get_game().change_scene(Constants.SCENES["PLAYING"])
                if event.key == pygame.K_RETURN:
                    game = self.get_game()
                    HighScore().add(self._player_name, game.get_score())
                    game.reset()
                    game.change_scene(Constants.SCENES["HIGH_SCORE"])
                elif 65 <= event.key <= 122:
                    self._player_name += chr(event.key)

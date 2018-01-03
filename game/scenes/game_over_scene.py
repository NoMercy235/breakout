from game.scenes.scene import Scene
from game.shared import Constants, pygame


class GameOverScene(Scene):

    def __init__(self, game):
        super().__init__(game)

    def render(self):
        super().render()

        self.clear_text()
        self.add_text("Press F1 to restart the game.", 400, 400, size=30)

    def handle_events(self, events):
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.get_game().reset()
                    self.get_game().change_scene(Constants.SCENES["PLAYING"])

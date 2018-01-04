from game.scenes.scene import Scene
from game.shared import Constants, pygame


class MenuScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.add_text("F1 - Start Game", x=300, y=200, size=30)
        self.add_text("F2 - Highscore", x=300, y=240, size=30)
        self.add_text("F3 - Quit", x=300, y=280, size=30)

        self._menu_sprite = pygame.image.load(Constants.SPRITES["MAIN_MENU"])

    def render(self):
        self.get_game().screen.blit(self._menu_sprite, (50, 50))

        super().render()

    def handle_events(self, events):
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.get_game().reset()
                    self.get_game().change_scene(Constants.SCENES["PLAYING"])
                if event.key == pygame.K_F2:
                    self.get_game().change_scene(Constants.SCENES["HIGH_SCORE"])
                if event.key == pygame.K_F3:
                    pygame.event.post(pygame.QUIT)

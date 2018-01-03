from game.shared import pygame


class Scene:

    def __init__(self, game):
        self._game = game
        self._texts = []

    def render(self):
        for text in self._texts:
            self._game.screen.blit(text[0], text[1])

    def get_game(self):
        return self._game

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

    def clear_text(self):
        self._texts = []

    def add_text(self, string, x=0, y=0, color=[255, 255, 255], background=[0, 0, 0, 0], size=17):
        font = pygame.font.Font(None, size)
        self._texts.append([font.render(string, True, color, background), (x, y)])

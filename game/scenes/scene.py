class Scene:

    def __init__(self, game):
        self._game = game
        self._texts = []

    def render(self):
        pass

    def get_game(self):
        return self._game

    def handle_events(self, events):
        pass

    def clear_text(self):
        self._texts = []

    def add_text(self, string, x=0, y=0, color=[255, 255, 255], background=[0, 0, 0, 0], size=17):
        pass

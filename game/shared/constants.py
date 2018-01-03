import os


class Constants:

    INITIAL_LIVES = 5
    SCREEN_SIZE = [800, 600]
    PAD_SIZE = [139, 13]
    FPS = 60
    BRICK = {
        "SIZE": [800, 600],
        "HP": 100,
        "LIVES": 1,
    }
    BALL = {
        "SIZE": [16, 16],
        "SPEED": 3,
    }

    SPRITES = {
        "BALL": os.path.join("assets", "ball.png"),
    }

    TEXTS = {
        "CAPTION": "Breakout in Python"
    }

import os


class Constants:

    INITIAL_LIVES = 5
    SCREEN_SIZE = [800, 600]
    PAD_SIZE = [139, 13]
    SPACE_BELOW_PAD = 50
    FPS = 60
    BRICK = {
        "SIZE": [100, 30],
        "HP": 100,
        "LIVES": 1,
    }
    BALL = {
        "SIZE": [16, 16],
        "SPEED": 3,
    }

    SPRITES = {
        "BALL": os.path.join("assets", "ball.png"),
        "BRICK-NORMAL": os.path.join("assets", "standard.png"),
        "BRICK-SPEED": os.path.join("assets", "speed.png"),
        "BRICK-LIFE": os.path.join("assets", "life.png"),
        "PAD": os.path.join("assets", "pad.png"),
    }

    TEXTS = {
        "CAPTION": "Breakout in Python"
    }

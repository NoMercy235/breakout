import os


class Constants:

    INITIAL_LIVES = 1
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
        "MAX_SPEED": 6,
        "SPEED_INCREASE": 1,
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

    SCENES = {
        "PLAYING": 0,
        "GAME_OVER": 1,
        "HIGH_SCORE": 2,
        "MAIN_MENU": 3,
    }

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
        "HIGH_SCORE": os.path.join("assets", "highscore.png"),
        "MAIN_MENU": os.path.join("assets", "menu.png"),
    }

    SOUNDS = {
        "GAME_OVER": (0, os.path.join("assets", "GameOver.wav")),
        "HIT_BRICK": (1, os.path.join("assets", "BrickHit.wav")),
        "HIT_BRICK_LIFE": (2, os.path.join("assets", "ExtraLife.wav")),
        "HIT_BRICK_SPEED": (3, os.path.join("assets", "SpeedUp.wav")),
        "HIT_WALL": (4, os.path.join("assets", "WallBounce.wav")),
        "HIT_PAD": (5, os.path.join("assets", "PadBounce.wav")),
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

# package pong.view.theme

from pong_game.model.Ball import Ball
from pong_game.view.Assets import Assets

"""
   Specific theme

   *** Nothing to do here ***
"""


class Duckie(Assets):
    # ------------ Handling Images ------------------------

    background = Assets.get_image("duckieBg.jpg")
    ball = "duckieBall.png"

    Assets.bind(Ball, "duckieBall.png")


    @classmethod
    def get_background(cls):
        return cls.background

    # -------------- Audio handling -----------------------------
    ball_hit_paddle_sound = "ballhitpaddle.wav"

    @classmethod
    def get_ball_hit_paddle_sound(cls):
        return cls.ball_hit_paddle_sound
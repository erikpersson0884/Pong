# package pong.view.theme

from pong_game.model.Ball import Ball
from pong_game.view.Assets import Assets

"""
   Specific theme

   *** Nothing to do here ***
"""


class Cool(Assets):
    # ------------ Handling Images ------------------------

    background = Assets.get_image("coolBg.png")

    Assets.bind(Ball, "coolBall.png")

    @classmethod
    def get_background(cls):
        return cls.background

    # -------------- Audio handling -----------------------------

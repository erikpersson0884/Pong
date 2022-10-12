# package pong.view.theme
import pygame
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
    ball_hit_paddle_sound = Assets.get_sound("ballhitpaddle.waw")

    @classmethod
    def get_ball_hit_paddle_sound(cls):
        return cls.ball_hit_paddle_sound
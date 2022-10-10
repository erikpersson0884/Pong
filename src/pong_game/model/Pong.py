# package pong.model

import pong_game.event.ModelEvent
import pong_game.event.EventBus

from pong_game.model.Ball import Ball
from pong_game.model.Paddle import Paddle


class Pong:
    """
     * Logic for the Pong Game
     * Model class representing the "whole" game
     * Nothing visual here
    """
    # TODO More attributes
    points_left  = 0
    points_right = 0

    # TODO Initialization
    def __init__(self, ball, paddle_left, paddle_right):
        self.__ball: Ball = ball
        self.__paddle_left: Paddle = paddle_left
        self.__paddle_right: Paddle = paddle_right
        pass

    # --------  Game Logic -------------

    timeForLastHit = 0         # To avoid multiple collisions

    def update(self, now):
        self.__move_the_ball()
        self.__move_the_left_paddle()
        self.__move_the_right_paddle()
        # TODO Game logic here
    
    def __move_the_left_paddle(self):
        #if
        self.__paddle_left.move()
    def __move_the_right_paddle(self):
        #if
        self.__paddle_right.move()
        
    def __move_the_ball(self):
        self.__ball.move() 
        
    # --- Used by GUI  ------------------------
    @classmethod
    def get_all_items_with_position(cls):
        drawables = []
        # TODO
        return drawables

    @classmethod
    def get_points_left(cls):
        return cls.points_left

    @classmethod
    def get_points_right(cls):
        return cls.points_right

    @classmethod
    def set_speed_right_paddle(cls, dy):
        # TODO
        pass

    @classmethod
    def set_speed_left_paddle(cls, dy):
        # TODO
        pass

# package pong.model

from enum import Enum, auto
from pong_game.event.ModelEvent import ModelEvent
import pong_game.event.EventBus

from pong_game.model.Ball import Ball
from pong_game.model.Config import GAME_WIDTH
from pong_game.model.Paddle import Paddle

class Pong:
    """
     * Logic for the Pong Game
     * Model class representing the "whole" game
     * Nothing visual here
    """
    class PaddleSide(Enum):
        NONE = auto()
        RIGHT = auto()
        LEFT = auto()    

    def __init__(self, ball, paddle_left, paddle_right):
        self.__ball: Ball = ball
        self.__paddle_left: Paddle = paddle_left
        self.__paddle_right: Paddle = paddle_right
        self.__points_left: int = 0
        self.__points_right: int = 0
        self.__last_hit: Pong.PaddleSide = Pong.PaddleSide.NONE

        self.event = ""


    # --------  Game Logic -------------
        # To avoid multiple collisions

    def update(self, now):
        self.__move_the_ball()
        self.__paddle_right.move()
        self.__paddle_left.move()
        self.check_collision_with_paddle()
        
        if 0 - self.__ball.get_width() > self.__ball.get_x():
            self.__points_right += 1
            self.reset_ball()
        
        elif GAME_WIDTH < self.__ball.get_x():
            self.__points_left += 1
            self.reset_ball()
            
    def reset_ball(self):
        self.__ball.reset_ball_pos()
        self.__ball.reset_direction()
        self.__ball.reset_speed()
        self.__last_hit = Pong.PaddleSide.NONE

    # def __move_the_left_paddle(self):
    #     self.__paddle_left.move()

    #def __move_the_right_paddle(self):
        #self.__paddle_right.move()
        
    def __move_the_ball(self):
        self.__ball.move() 
        
    # --- Used by GUI  ------------------------
    def get_all_items_with_position(self):
        drawables = []
        # TODO
        return drawables

    def get_points_left(self):
        return self.__points_left

    def get_points_right(self):
        return self.__points_right

    def move_the_paddle(self, dy: int, paddle: str):
        if paddle == "right":
            self.__paddle_right.set_direction(dy)

                
        elif paddle == "left":
            self.__paddle_left.set_direction(dy)

    # Nice utility method possibly useful for any positionable object
    # def intersects(self, other):
        # above = other.__get_max_y() < self.get_y()
        # below = other.get_y() > self.__get_max_y()
        # left_of = other.__get_max_x() < self.get_x()
        # right_of = other.get_x() > self.__get_max_x()
        # return not (above or below or left_of or right_of)

    def check_collision_with_paddle(self):
        # bounce interval for left paddle
        if self.__paddle_left.get_x() < self.__ball.get_x() < self.__paddle_left.get_x() + self.__paddle_left.get_width():
            if self.__paddle_left.get_y() + self.__paddle_left.get_height() >= self.__ball.get_y() \
            and self.__paddle_left.get_y() <= self.__ball.get_y() + self.__ball.get_height() \
            and self.__last_hit != Pong.PaddleSide.LEFT:
                self.event ="ball_hit_paddle"

                self.__ball.bounce()
                self.__ball.accelerate()
                self.__last_hit = Pong.PaddleSide.LEFT

        elif self.__paddle_right.get_x() + self.__paddle_right.get_width() > self.__ball.get_x() + self.__ball.get_width() > self.__paddle_right.get_x():
            if self.__paddle_right.get_y() + self.__paddle_right.get_height() >= self.__ball.get_y() \
            and self.__paddle_right.get_y() <= self.__ball.get_y() + self.__ball.get_height()\
            and self.__last_hit != Pong.PaddleSide.RIGHT:
                self.event ="ball_hit_paddle"

                self.__ball.bounce()
                self.__ball.accelerate()
                self.__last_hit = Pong.PaddleSide.RIGHT

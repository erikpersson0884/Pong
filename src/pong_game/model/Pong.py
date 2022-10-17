# package pong.model
from enum import Enum, auto

from pong_game.model.Ball import Ball
from pong_game.model.Config import GAME_WIDTH, GAME_HEIGHT
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
        self.__sound_event = ""


    # --------  Game Logic -------------
        # To avoid multiple collisions

        
    def update(self):
        self.__paddle_right.move()
        self.__paddle_left.move()
        self.__move_the_ball()
        self.check_ball_collision_with_floor_and_ceiling()
        self.check_ball_collision_with_paddle()
        self.check_if_ball_out_of_bounds()

    def check_ball_collision_with_floor_and_ceiling(self):
        above_floor = self.__ball.get_y() > GAME_HEIGHT - self.__ball.get_height()
        below_ceiling = 0 > self.__ball.get_y()

        if above_floor or below_ceiling:
            self.__ball.bounce_on_walls()

    def check_if_ball_out_of_bounds(self):
        is_past_left_paddle = 0 - self.__ball.get_width() > self.__ball.get_x()
        is_past_right_paddle = GAME_WIDTH < self.__ball.get_x()
        
        if is_past_left_paddle:
            self.__points_right += 1
            self.reset_ball()
        
        elif is_past_right_paddle:
            self.__points_left += 1
            self.reset_ball()
    
    def __move_the_ball(self):
        self.__ball.move() 

    def check_ball_collision_with_paddle(self):
        is_at_left_paddle = self.__ball.get_x() < self.__paddle_left.get_x() + self.__paddle_left.get_width() < self.__ball.get_old_x()
        is_at_right_paddle = self.__ball.get_old_x() + self.__ball.get_width() < self.__paddle_right.get_x() < self.__ball.get_x() + self.__ball.get_width()

        if is_at_left_paddle:
            is_not_over_paddle_left = self.__paddle_left.get_y() <= self.__ball.get_y() + self.__ball.get_height()
            is_not_under_paddle_left = self.__paddle_left.get_y() + self.__paddle_left.get_height() >= self.__ball.get_y()
            
            collides_with_paddle_left = is_not_under_paddle_left and is_not_over_paddle_left
            
            if collides_with_paddle_left and self.__last_hit != Pong.PaddleSide.LEFT:
                self.__last_hit = Pong.PaddleSide.LEFT        
                self.__ball.set_x(self.__paddle_left.get_x() + self.__paddle_left.get_width())
                self.ball_hits_paddle()

        elif is_at_right_paddle:
            is_not_under_right_paddle = self.__paddle_right.get_y() + self.__paddle_right.get_height() >= self.__ball.get_y()
            is_not_over_right_paddle = self.__paddle_right.get_y() <= self.__ball.get_y() + self.__ball.get_height()

            collides_with_paddle_right = is_not_under_right_paddle and is_not_over_right_paddle

            if collides_with_paddle_right and self.__last_hit != Pong.PaddleSide.RIGHT:
                self.__last_hit = Pong.PaddleSide.RIGHT     
                self.__ball.set_x(self.__paddle_right.get_x() - self.__ball.get_width())
                self.ball_hits_paddle()

    def ball_hits_paddle(self) -> None:
        self.__sound_event = "ball_hit_paddle"
        self.__ball.accelerate()
        self.__ball.bounce_on_paddle()

    def reset_ball(self) -> None:
        self.__ball.reset_ball_pos()
        self.__ball.reset_direction()
        self.__ball.reset_speed()
        self.__last_hit = Pong.PaddleSide.NONE

    # --- Used by GUI  ------------------------
    def get_pong_sound_event(self) -> str:
        return self.__sound_event

    def set_pong_sound_event(self, sound_event: str) -> None:
        self.__sound_event = sound_event

    def get_points_left(self) -> int:
        return self.__points_left

    def get_points_right(self) -> int:
        return self.__points_right

    def move_the_paddle(self, dy: int, paddle: str):
        if paddle == "right":
            self.__paddle_right.set_paddle_direction(dy)
            
        elif paddle == "left":
            self.__paddle_left.set_paddle_direction(dy)

# package pong.model

from pong_game.model.Config import GAME_WIDTH, GAME_HEIGHT
from pong_game.model.HasPosition import HasPosition
from random import uniform, choice
from math import sqrt
"""
 * A Ball for the Pong game
 * A model class
"""


class Ball(HasPosition):
    def __init__(self) -> None:
        super().__init__()
        self.__start_speed = 10
        
        self.__WIDTH = 40
        self.__HEIGHT = 40
        self.__x: int = self.__get_start_x()
        self.__y: int = self.__get_start_y()
        self.__old_x: float = self.__x

        self.__dx = self.__get_start_dx()
        self.__dy = self.__get_start_dy()

        self.__SPEED = self.__start_speed

    def __get_start_x(self) -> int:
        return int(GAME_WIDTH / 2 - self.get_width() / 2)

    def __get_start_y(self) -> int:
        return int(GAME_HEIGHT / 2 - self.get_height() / 2)

    def __get_start_dx(self):
        dx = choice([uniform(-1, -1/sqrt(2)), uniform(1/sqrt(2), 1)])
        return dx

    def __get_start_dy(self):
        return sqrt(1 - (self.__dx) ** 2)

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):      # Min x and y is upper left corner (y-axis pointing down)
        return self.__x

    def get_y(self):
        return self.__y

    def get_old_x(self):
        return self.__old_x

    def get_width(self):
        return self.__WIDTH

    def get_height(self):
        return self.__HEIGHT

    def move(self):
        self.__old_x = self.get_x()
        self.set_x(self.get_x() + self.__dx * self.__SPEED)
        self.set_y(self.get_y() + self.__dy * self.__SPEED)
        if 0 > self.__y or self.__y > GAME_HEIGHT - self.get_height():
            self.__dy *= -1
    
    def reset_ball_pos(self):
        self.__x = self.__get_start_x()
        self.__y = self.__get_start_y()

    def reset_speed(self):
        self.__SPEED = self.__start_speed
    
    def reset_direction(self):
        self.__dx = self.__get_start_dx()
        self.__dy = self.__get_start_dy()

    def bounce(self):
        self.__dx *= -1
    
    def accelerate(self):
        self.__SPEED *= 1.05
    




    def get_dx(self):      # Min x and y is upper left corner (y-axis pointing down)
        return self.__dx
    def get_SPEED(self):      # Min x and y is upper left corner (y-axis pointing down)
        return self.__SPEED
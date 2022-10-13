# package pong.model

from pong_game.model.Config import GAME_WIDTH, GAME_HEIGHT
from pong_game.model.HasPosition import HasPosition
from random import uniform, choice, randint
from math import sqrt
from pong_game.model.Moveable import Moveable

"""
 * A Ball for the Pong game
 * A model class
"""


class Ball(Moveable):
    def __init__(self) -> None:
        super().__init__()
        self.__WIDTH = 40
        self.__HEIGHT = 40
        self.__x: int = self.__get_start_x()
        self.__y: int = self.__get_start_y()
        self.__old_x: float = self.__x

        self.__dx = self.__get_start_dx()
        self.__dy = self.__get_start_dy()

        self.__speed = 8
        self.__SPEED_FACTOR = 1.05 

    def __get_start_x(self) -> int:
        return int(GAME_WIDTH / 2 - self.get_width() / 2)

    def __get_start_y(self) -> int:
        return int(GAME_HEIGHT / 2 - self.get_height() / 2)

    def __get_start_dx(self) -> float:
        possible_directions = [uniform(-1, -1/sqrt(2)), uniform(1/sqrt(2), 1)]
        dx = choice(possible_directions)
        return dx

    def __get_start_dy(self) -> float:
        return sqrt(1 - (self.__dx) ** 2)

    def get_x(self) -> float:      # Min x and y is upper left corner (y-axis pointing down)
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def get_old_x(self) -> float:
        return self.__old_x

    def get_width(self) -> int:
        return self.__WIDTH

    def get_height(self) -> int:
        return self.__HEIGHT


    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    
    def move(self):
        self.__old_x = self.get_x()
        self.set_x(self.get_x() + self.__dx * self.__speed)
        self.set_y(self.get_y() + self.__dy * self.__speed)

        if 0 > self.__y or self.__y > GAME_HEIGHT - self.get_height():
            self.__dy *= -1
    
    def reset_ball_pos(self):
        self.__x = self.__get_start_x()
        self.__y = self.__get_start_y()

    def reset_speed(self):
        self.__speed = randint(10, 15)
    
    def reset_direction(self):
        self.__dx = self.__get_start_dx()
        self.__dy = self.__get_start_dy()

    def bounce(self):
        self.__dx *= -1
    
    def accelerate(self):
        self.__speed *= self.__SPEED_FACTOR

    def get_dx(self) -> float:      # Min x and y is upper left corner (y-axis pointing down)
        return self.__dx
        
    def get_speed(self) -> float:      # Min x and y is upper left corner (y-axis pointing down)
        return self.__speed
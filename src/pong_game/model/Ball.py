# package pong.model

from pong_game.model.Config import GAME_WIDTH, GAME_HEIGHT
from random import uniform, choice, randint
from math import sqrt
from pong_game.model.Moveable import Moveable

"""
 * A Ball for the Pong game
 * A model class
"""

class Ball(Moveable):
    BALL_WIDTH = 40
    BALL_HEIGHT = 40

    def __init__(self) -> None:
        super().__init__(x = self.__get_start_x(), y = self.__get_start_y(), WIDTH = self.BALL_WIDTH, HEIGHT = self.BALL_HEIGHT, speed = 10)
        self.__old_x: float = self.get_x()
        self.__dx: float = self.__get_start_dx()
        self.__dy: float = self.__get_start_dy()
        self.__SPEED_FACTOR: float = 1.05 

    def __get_start_x(self) -> int:
        return int(GAME_WIDTH / 2 - self.BALL_WIDTH / 2)

    def __get_start_y(self) -> int:
        return int(GAME_HEIGHT / 2 - self.BALL_HEIGHT / 2)
        
    @staticmethod
    def __get_start_dx() -> float:
        possible_directions = [uniform(-1, -1/sqrt(2)), uniform(1/sqrt(2), 1)]
        dx = choice(possible_directions)
        return dx
    
    def __get_start_dy(self) -> float:
        return sqrt(1 - (self.__dx) ** 2)

    def get_old_x(self) -> float:
        return self.__old_x

    def get_dx(self) -> float:      
        return self.__dx

    def get_dy(self) -> float:      
        return self.__dy

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    def move(self):
        self.__old_x = self.get_x()
        self.set_x(self.get_x() + self.get_dx() * self.get_speed())
        self.set_y(self.get_y() + self.get_dy() * self.get_speed())

    def bounce_on_paddle(self):
        self.set_dx(self.get_dx() * (-1))
    
    def bounce_on_walls(self):
        self.set_dy(self.get_dy() * (-1))
    
    def accelerate(self):
        self.set_speed(self.get_speed() * self.__SPEED_FACTOR)
    
    def reset_ball_pos(self):
        self.set_x(self.__get_start_x())
        self.set_y(self.__get_start_y())

    def reset_speed(self):
        self.set_speed(randint(10, 15))
    
    def reset_direction(self):
        self.set_dx(self.__get_start_dx())
        self.set_dy(self.__get_start_dy())

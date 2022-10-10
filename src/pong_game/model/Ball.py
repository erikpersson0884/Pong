# package pong.model

from pong_game.model.Config import GAME_WIDTH, GAME_HEIGHT
from pong_game.model.HasPosition import HasPosition
"""
 * A Ball for the Pong game
 * A model class
"""


class Ball(HasPosition):
    def __init__(self) -> None:
        super().__init__()

        self.__WIDTH = 40
        self.__HEIGHT = 40
        self.__x: int = self.__get_start_x()
        self.__y: int = self.__get_start_y()

        self.__dx = 0
        self.__dy = 0

    def set_dx(self, dx):
        self.__dx = dx

    def move(self):
        self.set_x(self.get_x() + self.__dx)

    def set_x(self, x):
        self.__x = x

    def get_x(self):      # Min x and y is upper left corner (y-axis pointing down)
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__WIDTH

    def get_height(self):
        return self.__HEIGHT

    def __get_start_x(self) -> int:
        return int(GAME_WIDTH / 2 - self.get_width() / 2)

    def __get_start_y(self) -> int:
        return int(GAME_HEIGHT / 2 - self.get_height() / 2)
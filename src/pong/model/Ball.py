# package pong.model

from pong.model.Config import GAME_WIDTH, GAME_HEIGHT
from HasPosition import HasPosition
"""
 * A Ball for the Pong game
 * A model class
"""


class Ball(HasPosition):

    def __init__(self) -> None:
        super().__init__()

        self.__WIDTH = 40
        self.__HEIGHT = 40
        self.__x: int = 0
        self.__y: int = 0


    def get_x(self):      # Min x and y is upper left corner (y-axis pointing down)
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__WIDTH

    def get_height(self):
        return self.__HEIGHT

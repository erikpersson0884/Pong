# package pong.model

from abc import ABC


class HasPosition(ABC):
    """
        Contract for anything that can be positioned in the world.

        NOTE: This must be fulfilled by any object the GUI shall render
    """
    def __init__(self, x, y, WIDTH, HEIGHT):
        self.__x: float = x
        self.__y:float = y
        self.__WIDTH: int = WIDTH
        self.__HEIGHT: int = HEIGHT
        
    def get_x(self) -> float:      # Min x and y is upper left corner (y-axis pointing down)
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def set_x(self, x: float) -> None:
        self.__x = x

    def set_y(self, y: float) -> None:
        self.__y = y

    def get_width(self) -> int:
        return self.__WIDTH

    def get_height(self) -> int:
        return self.__HEIGHT

    def set_height(self, height: int) -> None:
        self.__HEIGHT = height

    def set_width(self, width: int) -> None:
        self.__WIDTH = width




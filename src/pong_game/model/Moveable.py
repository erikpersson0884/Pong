from pong_game.model.HasPosition import HasPosition
from abc import ABC, abstractmethod

class Moveable(HasPosition, ABC):
    def __init__(self, x, y, WIDTH, HEIGHT, speed):
        super().__init__(x, y, WIDTH, HEIGHT)
        self.__speed = speed

    @abstractmethod
    def move(self):
        raise NotImplementedError

    def get_speed(self) -> float:  # Min x and y is upper left corner (y-axis pointing down)
        return self.__speed

    def set_speed(self, new_speed):
        self.__speed = new_speed
    
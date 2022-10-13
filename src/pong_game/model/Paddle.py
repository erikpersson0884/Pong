# package pong.model

from pong_game.model.Config import GAME_HEIGHT
from pong_game.model.HasPosition import HasPosition
from pong_game.model.Moveable import Moveable

# A Paddle for the Pong game
class Paddle(Moveable):
    def __init__(self, x) -> None:
        super().__init__()
        self.__WIDTH = 10
        self.__HEIGHT = 60
        self.__x = x
        self.__y = self.__get_start_y()
        self.__direction = 0
        self.__SPEED = 10
    
    def __get_start_y(self) -> int:
        return int(GAME_HEIGHT / 2 - self.__HEIGHT / 2)

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_width(self) -> int:
        return self.__WIDTH

    def get_height(self) -> int:
        return self.__HEIGHT
    
    def get_paddle_direction(self) -> int:
        return self.__direction

    def set_paddle_direction(self, direction: int):
        self.__direction = direction


    def move(self):
        if self.__direction == -1 and 0 < self.__y:
            self.__y += self.__direction * self.__SPEED

        elif self.__direction == 1 and self.__y < GAME_HEIGHT - self.get_height():
            self.__y += self.__direction * self.__SPEED 
    
            
    def set_direction(self, direction: int):
        self.__direction = direction

    def stop(self):
        self.set_direction(0)



# package pong.model

from pong_game.model.Config import GAME_HEIGHT
from pong_game.model.HasPosition import HasPosition

# A Paddle for the Pong game
class Paddle(HasPosition):
    def __init__(self) -> None:
        super().__init__()
        self.__x = 0
        self.__y = GAME_HEIGHT/2
        self.__WIDTH = 10
        self.__HEIGHT = 60
        self.__SPEED = 5


    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__WIDTH

    def get_height(self):
        return self.__HEIGHT
    
    def get_paddle_speed(self):
        return self.__SPEED
    
    def move_up(self):
        if self.__y > 0:
            self.__y -= self.__SPEED

    def move_down(self):
        if self.__y < GAME_HEIGHT:
            self.__y += self.__SPEED

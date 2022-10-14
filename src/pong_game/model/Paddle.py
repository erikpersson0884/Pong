# package pong.model

from pong_game.model.Config import GAME_HEIGHT
from pong_game.model.Moveable import Moveable

# A Paddle for the Pong game
class Paddle(Moveable):
    PADDLE_HEIGHT = 60
    PADDLE_WIDTH = 10

    def __init__(self, x) -> None:
        super().__init__(x, y = self.get_start_y(), WIDTH = self.PADDLE_WIDTH, HEIGHT = self.PADDLE_HEIGHT, speed = 10)
        self.__direction = 0

    def get_start_y(self) -> int:
        return int(GAME_HEIGHT / 2 - self.PADDLE_HEIGHT / 2)

    def get_paddle_direction(self) -> int:
        return self.__direction

    def set_paddle_direction(self, direction: int):
        self.__direction = direction

    def move(self):
        below_ceiling = 0 < self.get_y()
        above_floor = self.get_y() < GAME_HEIGHT - self.PADDLE_HEIGHT

        if (self.get_paddle_direction() == -1 and below_ceiling) or (self.get_paddle_direction() == 1 and above_floor):
            self.set_y(self.get_y() + self.get_paddle_direction() * self.get_speed())
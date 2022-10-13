from pong_game.model.HasPosition import HasPosition
from abc import ABC, abstractmethod

class Moveable(HasPosition, ABC):
    @abstractmethod
    def move(self):
        raise NotImplementedError
    
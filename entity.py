from abc import ABC, abstractmethod

from grid_point import GridPoint
from polygon import Polygon


class Entity(ABC):
    def __init__(self, x: int, y: int):
        super().__init__()
        self._position = GridPoint(x, y)

    @abstractmethod
    def draw(self) -> Polygon:
        pass

    @property
    def position(self) -> GridPoint:
        return self._position.clone()

    @property
    def x(self) -> int:
        return self._position.x

    @property
    def y(self) -> int:
        return self._position.y

    @position.setter
    def position(self, rhs: GridPoint):
        self._position = rhs.clone()

    @x.setter
    def x(self, rhs: int):
        self._position.x = rhs

    @y.setter
    def y(self, rhs: int):
        self._position.y = rhs

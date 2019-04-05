from random import randint

from colors import RED
from grid_point import GridPoint
from moveable import Moveable
from polygon import Polygon, SQUARE
from velocity import Velocity, DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT


class Wanderer(Moveable):
    def __init__(self, pos: GridPoint = None, wait_prob=1):
        super().__init__(pos, None)
        self._poly = SQUARE.clone()
        self._poly.color = RED
        self._max_rand = 3

        if wait_prob > 1:
            self._max_rand += wait_prob

    def draw(self) -> Polygon:
        return self._poly

    def move(self):
        direction = randint(0, self._max_rand)

        if direction == DIR_UP:
            dx = 0
            dy = -1
        elif direction == DIR_RIGHT:
            dx = +1
            dy = 0
        elif direction == DIR_DOWN:
            dx = 0
            dy = +1
        elif direction == DIR_LEFT:
            dx = -1
            dy = 0
        else:
            dx = 0
            dy = 0

        self._velocity.dx = dx
        self._velocity.dy = dy
        super().move()

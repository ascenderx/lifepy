from random import randint

from colors import RED
from grid_point import GridPoint
from moveable import Moveable
from polygon import Polygon, SQUARE
from velocity import Velocity


DIR_NONE = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4


class Wanderer(Moveable):
    def __init__(self, pos: GridPoint = None, vel: Velocity = None):
        super().__init__(pos, vel)
        self._poly = SQUARE.clone()
        self._poly.color = RED

    def draw(self) -> Polygon:
        return self._poly

    def move(self):
        direction = randint(0, 4)

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

        self._velocity = Velocity(dx, dy)
        super().move()

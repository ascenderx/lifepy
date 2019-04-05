from random import randint

from colors import GREEN
from draw_handler import DrawData
from grid_point import GridPoint
from moveable import Moveable
from polygon import DIAMOND
from velocity import DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT


class Wanderer(Moveable):
    DRAW_DATA = DrawData(
        DIAMOND.clone(),
        GREEN,
        False
    )

    def __init__(self, pos: GridPoint = None, wait_prob=1):
        super().__init__(pos, None)
        self._max_rand = 3

        if wait_prob > 1:
            self._max_rand += wait_prob

    def draw(self) -> DrawData:
        return Wanderer.DRAW_DATA

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

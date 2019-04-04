from colors import RED
from entity import Entity
from polygon import Polygon, SQUARE


class Wanderer(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self._poly = SQUARE.clone()
        self._poly.color = RED

    def draw(self) -> Polygon:
        return self._poly

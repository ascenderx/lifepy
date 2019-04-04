class GridPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, rhs):
        self._x = rhs

    @y.setter
    def y(self, rhs):
        self._y = rhs

    def clone(self):
        return GridPoint(self._x, self._y)

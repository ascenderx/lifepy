class Velocity:
    def __init__(self, dx: int = 0, dy: int = 0):
        self._dx = dx
        self._dy = dy

    @property
    def dx(self) -> int:
        return self._dx

    @property
    def dy(self) -> int:
        return self._dy

    @dx.setter
    def dx(self, rhs: int):
        self._dx = rhs

    @dy.setter
    def dy(self, rhs: int):
        self._dy = rhs

    def clone(self):
        return Velocity(self._dx, self._dy)

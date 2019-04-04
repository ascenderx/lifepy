from colors import WHITE


class Polygon:
    def __init__(self, *points, **kwargs):
        self._points = (*points,)
        self._color = WHITE
        self._filled = False

        for key, value in kwargs.items():
            if key == "color":
                self._color = value
            elif key == "fill" or key == "filled":
                self._filled = value
            else:
                raise KeyError(f'Unknown keyword argument "{key}"')

    def __iter__(self):
        return self._points.__iter__()

    @property
    def points(self) -> tuple:
        return self._points

    @property
    def color(self) -> tuple:
        return self._color

    @property
    def filled(self) -> bool:
        return self._filled

    @color.setter
    def color(self, rhs: tuple):
        self._color = (*rhs,)

    @filled.setter
    def filled(self, rhs: bool):
        self._filled = rhs

    def clone(self):
        return Polygon(*self._points, color=self._color, filled=self._filled)


SQUARE = Polygon(
    (0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0),
)
DIAMOND = Polygon(
    (0.5, 0.0), (1.0, 0.5), (0.5, 1.0), (0.0, 0.5),
)
TRIANGLE_N = Polygon(
    (0.0, 1.0), (0.5, 0.0), (1.0, 1.0),
)
TRIANGLE_E = Polygon(
    (0.0, 0.0), (1.0, 0.5), (0.0, 1.0),
)
TRIANGLE_S = Polygon(
    (1.0, 0.0), (0.5, 1.0), (0.0, 0.0),
)
TRIANGLE_W = Polygon(
    (1.0, 1.0), (0.0, 0.5), (1.0, 0.0),
)

from colors import *


class DrawHandler:
    def __init__(self, screen, grid, **kwargs):
        self._screen = screen
        self._grid = grid
        self._bg_color = BLACK

        for key, value in kwargs.items():
            if key == "bg_color":
                self._bg_color = value
            else:
                raise KeyError(f"Unknown keyword argument {key}")

    def update(self):
        # draw background
        self._screen.fill(self._bg_color)

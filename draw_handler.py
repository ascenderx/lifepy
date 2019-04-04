import pygame

from colors import *
from grid import Grid


class DrawHandler:
    def __init__(self, screen: pygame.Surface, grid: Grid, entities: list, **kwargs):
        self._screen = screen
        self._grid = grid
        self._entities = entities
        self._bg_color = BLACK
        self._line_width = 2

        for key, value in kwargs.items():
            if key == "bg_color":
                self._bg_color = value
            elif key == "line_width":
                self._line_width = value
            else:
                raise KeyError(f'Unknown keyword argument "{key}"')

    def update(self):
        # draw background
        self._screen.fill(self._bg_color)

        # draw entities
        for entity in self._entities:
            poly = entity.draw()
            pos = entity.position
            color = poly.color
            pixels = [self._grid.compute_pixel(
                pos.x + pt[0], pos.y + pt[1]
            ) for pt in poly]
            if poly.filled:
                line_w = 0
            else:
                line_w = self._line_width

            pygame.draw.polygon(self._screen, color, pixels, line_w)

        pygame.display.flip()

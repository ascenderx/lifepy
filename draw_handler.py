import pygame

from colors import *
from grid import Grid


class DrawHandler:
    def __init__(self, screen: pygame.Surface, grid: Grid, entities: list, **kwargs):
        self._screen = screen
        self._grid = grid
        self._entities = entities
        self._bg_color = BLACK

        for key, value in kwargs.items():
            if key == "bg_color":
                self._bg_color = value
            else:
                raise KeyError(f'Unknown keyword argument "{key}"')

    def update(self):
        # draw background
        self._screen.fill(self._bg_color)

        # draw entities
        for entity in self._entities:
            poly = entity.draw()
            pos = entity.position
            pixels = [self._grid.compute_pixel(pt[0], pt[1]) for pt in poly]


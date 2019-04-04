import pygame

from draw_handler import DrawHandler
from grid import Grid


class Game:
    def __init__(self):
        # display settings
        self._scr_w = 400
        self._scr_h = 400
        self._grid_w = 100
        self._grid_h = 100
        scr_dims = (self._scr_w, self._scr_h)
        self._screen = pygame.display.set_mode(scr_dims)
        self._grid = Grid(self._scr_w, self._scr_h, self._grid_w, self._grid_h)

        # handlers
        self._hdl_draw = DrawHandler(self._screen, self._grid)

        # timer settings
        self._framerate = 20
        self._interval = 1000 // self._framerate

        # game settings
        self._paused = False

    def _handle_input(self) -> bool:
        for event in pygame.event.get():
            # X window button -> quit
            if event.type == pygame.QUIT:
                return False

            # discrete keyboard input
            elif event.type == pygame.KEYUP:
                if event.mod & pygame.KMOD_CTRL:
                    # Ctrl + Q or Ctrl + W -> quit
                    if event.key == pygame.K_q or event.key == pygame.K_w:
                        return False
                elif event.mod & pygame.KMOD_ALT:
                    # Alt + F4 -> quit
                    if event.key == pygame.K_F4:
                        return False

                # P -> pause
                elif event.key == pygame.K_p:
                    self._paused = not self._paused

        return True

    def run(self):
        while True:
            # wait a bit before proceeding in order to give a more
            # arcade-like animation effect
            pygame.time.delay(self._interval)

            # get input
            running = self._handle_input()
            if not running:
                break

            # update the grid

            # draw the grid


if __name__ == "__main__":
    game = Game()
    game.run()

import random
import pygame
import math

from vector import *
from color_utils import *
from global_values import *

class Particle:
    '''
    A physics-driven particle that can move around the screen.

    If the particle's

        special
    variable is true, it will not reset and it will be shown with
    color as a ball, and not a curve.
    '''
    def __init__(self, pos: list = None, special = False):
        self.tales = []
        self.special = special
        self.reset(pos)
        self.color = random_color() if special else (255, 255, 255)

    def reset(self, pos: list = None):
        '''
        Resets the position of the particle to a random position
        on the display if a position is not given.

        If the particle is special, the particle does not get a
        
            max_len, life_len or a tale.
        '''
        self.pos = Vector(
            [
                random.uniform(0, screen_w),
                random.uniform(0, screen_h)
            ]
            if pos is None else pos
        )

        if (self.special):
            return

        self.max_len = 30
        self.life_left = random.uniform(self.max_len / 2, self.max_len)

        self.tales.append([])

    def update(self, vel: Vector):
        '''
        Updates the position of the particle given a velocity vector.

        If the particle is not special, it will get reset if

            life_len <= 0

        or if it's outside of the display
        '''
        self.pos += vel

        if self.special:
            return

        if self.life_left <= 0 or self.out_of_bounds(self.pos):
            self.reset()

    @property
    def life_value(self):
        '''
        A float (0-1) that represent how alive a particle is.
        If its at its end of its life, it will return 0 and 1
        if it has lots of life left.
        '''
        return self.life_left / self.max_len
    
    def out_of_bounds(self, pos: Vector):
        return pos.x > screen_w or pos.x < 0 or pos.y > screen_h or pos.y < 0

    def show(self, screen):
        '''
        Draws a circle at its position if the particle is not special.

        Else, it draws its tale, appends to the tale, and remove the
        previous tale's end if it exists.
        '''

        if self.special:
            x, y = self.pos.rounded
            pygame.draw.circle(screen, self.color, (x, screen_h - y), 10)
            return
        
        self.tales[-1].append(self.pos)
        self.life_left -= 1

        for _ in range(len(self.tales) - 1):
            if len(self.tales[0]) > 0:
                del self.tales[0][0]
            else:
                del self.tales[0]

        for tale in self.tales:
            for i in range(len(tale) - 1):
                pos1 = tale[i]
                pos2 = tale[i + 1]

                if self.out_of_bounds(pos2):
                    continue

                x1, y1 = pos1.rounded
                x2, y2 = pos2.rounded

                alpha = i / len(tale)
                color = color_with_alpha(self.color, alpha)

                pygame.draw.line(screen, color,
                                 (x1, screen_h - y1), (x2, screen_h - y2), 3)

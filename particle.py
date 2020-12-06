import random
import pygame
import math

from vector import *
from color_utils import *


class Particle:
    def __init__(self, size: list, pos: list = None):
        self.size = size
        self.tales = []
        self.reset(pos)
        self.color = random_color()

    def reset(self, pos: list = None):
        self.max_len = 2000
        # random.uniform(self.max_len / 2, self.max_len)
        self.life_left = self.max_len
        w, h = self.size
        self.pos = Vector(
            [
                random.uniform(0, w),
                random.uniform(0, h)
            ]
            if pos is None else pos
        )

        self.tales.append([])

    def update(self, vel: Vector):
        self.pos += vel

        w, h = self.size

        if self.life_left <= 0:  # or self.pos.get_sq_mag() > w**2 + h**2:
            self.reset()

    @property
    def life_value(self):
        return self.life_left / self.max_len

    def show(self, screen):
        self.tales[-1].append(self.pos)
        self.life_left -= 1

        for _ in range(len(self.tales) - 1):
            if len(self.tales[0]) > 0:
                del self.tales[0][0]
            else:
                del self.tales[0]

        w, h = self.size
        for tale in self.tales:
            for i in range(len(tale) - 1):
                pos1 = tale[i]
                pos2 = tale[i + 1]

                if pos2.get_sq_mag() > w**2 + h**2:
                    continue

                x1, y1 = tuple([round(x) for x in pos1.array])
                x2, y2 = tuple([round(x) for x in pos2.array])

                alpha = i / len(tale)
                color = color_with_alpha(self.color, alpha)

                pygame.draw.line(screen, color,
                                 (x1, h - y1), (x2, h - y2), 3)

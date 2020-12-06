import random
import pygame
import math

from vector import *
from color_utils import *


class Particle:
    def __init__(self, size: list, pos: list = None, special = False):
        self.size = size
        self.tales = []
        self.special = special
        self.reset(pos)
        self.color = random_color() if special else (255, 255, 255)

    def reset(self, pos: list = None):
        w, h = self.size
        self.pos = Vector(
            [
                random.uniform(0, w),
                random.uniform(0, h)
            ]
            if pos is None else pos
        )

        if (self.special):
            return

        self.max_len = 30
        self.life_left = random.uniform(self.max_len / 2, self.max_len)
        w, h = self.size

        self.tales.append([])

    def update(self, vel: Vector):
        self.pos += vel

        if self.special:
            return

        w, h = self.size
        if self.life_left <= 0 or self.pos.get_sq_mag() > w**2 + h**2:
            self.reset()

    @property
    def life_value(self):
        return self.life_left / self.max_len

    def show(self, screen):
        w, h = self.size

        if self.special:
            x, y = self.pos.rounded
            pygame.draw.circle(screen, self.color, (x, h - y), 10)
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

                if pos2.get_sq_mag() > w**2 + h**2:
                    continue

                x1, y1 = pos1.rounded
                x2, y2 = pos2.rounded

                alpha = i / len(tale)
                color = color_with_alpha(self.color, alpha)

                pygame.draw.line(screen, color,
                                 (x1, h - y1), (x2, h - y2), 3)

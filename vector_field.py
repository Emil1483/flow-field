from numpy import arange
import pygame

from vector import *
from particle import *


class Vector_Field:
    def __init__(self, screen, size: list, function):
        '''
        screen, size, function
        pass in function of type

            Vector(px, py) => Vector(x, y)

        pass in screen size of type

            [width, height]
        '''
        self.screen = screen
        self.size = size

        self.function = function
        self.particles = [Particle(size) for _ in range(1)]

    def show(self):
        # w, h = self.size

        # space = w / 20

        # middle = Vector([w / 2, h / 2])
        # for y in arange(space / 2, h, space):
        #     for x in arange(space / 2, w, space):
        #         pos = Vector([x, y])
        #         Vector(self.function(pos - middle).array).show(self.screen, pos)

        for particle in self.particles:
            particle.show(self.screen)

    def update(self):
        for particle in self.particles:
            particle.update(self.function(particle.pos))
    
    def add_particle(self, particle):
        if (len(self.particles) >= 3):
            del self.particles[0] 
        self.particles.append(particle)
    
    def remove_particle(self):
        if len(self.particles) is 0:
            return
        del self.particles[0]

from numpy import arange
import pygame

from vector import *
from particle import *


class Vector_Field:
    '''
    Stores a field such that each (x, y) position in the field
    corresponds with a vector given by function

        f(pos: Vector): Vector

    This object also manages an array of particles that travels
    in the vector field.
    '''
    def __init__(self, screen, size: list, function):
        self.screen = screen
        self.size = size

        self.function = function
        self.particles = [Particle(size) for _ in range(70)]

    def show(self):
        '''
        Renders the particles
        '''
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
        '''
        Updates the particles by setting their velocities
        to their corresponding vector in the vector field
        '''
        for particle in self.particles:
            particle.update(self.function(particle.pos))
    
    def add_particle(self, particle):
        '''
            Adds a special particle to the stored particles

            Raises an exception if given particle is not special
        '''
        if not particle.special:
            raise Exception('please only add special particles')
        if self.particles[0].special:
            del self.particles[0] 
        self.particles.insert(0, particle)
    
    def remove_particle(self):
        if not self.particles[0].special:
            return
        del self.particles[0]

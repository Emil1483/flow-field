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
    def __init__(self, screen, function):
        self.sound_on_add = pygame.mixer.Sound('funny.wav')
        self.sound_on_remove = pygame.mixer.Sound('funny2.wav')

        self.screen = screen

        self.function = function
        self.particles = [Particle() for _ in range(70)]

    def show(self):
        '''
        Renders the particles
        '''

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
        self.sound_on_add.play()
    
    def remove_particle(self):
        '''
        Removes the first particle if it is special
        '''
        if not self.particles[0].special:
            return
        del self.particles[0]
        self.sound_on_remove.play()

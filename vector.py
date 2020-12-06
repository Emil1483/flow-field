import functools
import math
import pygame
import colorsys

class Vector:
    def __init__(self, array):
        self.array = array

    def __add__(self, vector):
        if len(self.array) != len(vector.array):
            raise Exception('vectors must be the same size')

        array = []
        for i in range(len(self.array)):
            array.append(self.array[i] + vector.array[i])
        return Vector(array)

    @property
    def x(self):
        return self.array[0]

    @property
    def y(self):
        return self.array[1]
    
    @property
    def rounded(self):
        return [round(x) for x in self.array]

    def scale(self, scalar):
        return Vector([element * scalar for element in self.array])

    def div(self, dividend):
        return self.scale(1 / dividend)

    def __sub__(self, vector):
        return self + vector.scale(-1)

    def get_sq_mag(self):
        squared_array = [element**2 for element in self.array]
        squared_array_sum = functools.reduce(lambda a, b: a + b, squared_array)
        return squared_array_sum

    def get_mag(self):
        return math.sqrt(self.get_sq_mag())

    def normalize(self):
        return self.div(self.get_mag())
    
    def show(self, screen, pos):
        mag = self.get_mag()
        a = mag * 255
        scale = 50
        pygame.draw.line(screen, (a, a, a), pos.array, (pos + self.scale(scale)).array)
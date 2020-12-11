import functools
import math
import pygame

class Vector:
    '''
    This is a wrapper for an array such that it behaves like a vector.
    Matrix transformation is not implemented.
    '''

    def __init__(self, array):
        self.array = array

    def __add__(self, vector):
        '''
        adds each element of vector1 to each element of array2
        '''
        if len(self.array) != len(vector.array):
            raise Exception('vectors must be the same size')

        array = []
        for i in range(len(self.array)):
            array.append(self.array[i] + vector.array[i])
        return Vector(array)

    @property
    def x(self):
        '''
        returns the first element of the array
        '''
        return self.array[0]

    @property
    def y(self):
        '''
        returns the second element of the array
        '''
        return self.array[1]
    
    @property
    def rounded(self):
        '''
        returns an array where each element is its corresponding element
        in the original array rounded to the nearest integer.
        '''
        return [round(x) for x in self.array]

    def scale(self, scalar):
        '''
        returns a vector that is the original vector scaled by some scalar
        '''
        return Vector([element * scalar for element in self.array])

    def div(self, dividend):
        '''
        returns a vector that is the original vector scaled by 1/scalar
        '''
        return self.scale(1 / dividend)

    def __sub__(self, vector):
        '''
        subtracts each element of vector1 with each element in vector2
        '''
        return self + vector.scale(-1)

    def get_sq_mag(self):
        '''
        return the square of the magnitude
        '''
        squared_array = [element**2 for element in self.array]
        squared_array_sum = functools.reduce(lambda a, b: a + b, squared_array)
        return squared_array_sum

    def get_mag(self):
        '''
        returns the magnitude of the vector
        '''
        return math.sqrt(self.get_sq_mag())

    def normalize(self):
        '''
        returns a vector with the same direction as the original,
        but with a magnitude of 1.
        '''
        return self.div(self.get_mag())
    
    def show(self, screen, pos):
        '''
        uses pygame to draw a line at position pos with a constant length,
        but with the same angle as the vector.
        '''
        mag = self.get_mag()
        a = mag * 255
        scale = 50
        pygame.draw.line(screen, (a, a, a), pos.array, (pos + self.scale(scale)).array)
from vector import *


def transform(pos: Vector, size: list):
    '''
    Transforms a vector to a new vector. This is
    used to scale and translate the vector field.
    '''
    w, h = size
    return (pos - Vector([w / 2, h / 2])).div(100)

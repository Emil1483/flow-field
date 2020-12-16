from vector import *
from global_values import *


def transform(pos: Vector):
    '''
    Transforms a vector to a new vector. This is
    used to scale and translate the vector field.
    '''
    return (pos - Vector([screen_w / 2, screen_h / 2])).div(100)

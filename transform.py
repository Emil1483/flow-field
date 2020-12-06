from vector import *


def transform(pos: Vector, size: list):
    w, h = size
    return (pos - Vector([w / 2, h / 2])).div(100)

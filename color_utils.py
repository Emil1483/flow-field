import random


def random_color():
    index = random.randint(0, 2)
    return tuple([255 if index == i else random.uniform(0, 255)
                  for i in range(3)])

def color_with_alpha(color, alpha):
    return tuple([c * alpha for c in color])
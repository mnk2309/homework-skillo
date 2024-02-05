import numpy as np


def square_area(side_lenght):
    return side_lenght ** 2


def triangle_area(base, height):
    return 0.5 * base * height


def rectangular_area(length, width):
    return length * width


def circle_area(radius):
    return np.pi * radius ** 2


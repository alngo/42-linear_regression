import numpy as np


def mean_squared_error(p0, p1, X, y):
    cost = ((p0 + (p1 * X)) - y) * ((p0 + (p1 * X)) - y)
    return sum((1 / (2 * len(X))) * cost)


def normalize(list):
    minValue = min(list)
    maxValue = max(list)
    newList = (list - minValue) / (maxValue - minValue)
    return [newList, minValue, maxValue]


def scale(value, min, max):
    return np.float64((value * (max - min)) + min)


def upscale(value, min, max):
    return np.float64((value - min) / (max - min))

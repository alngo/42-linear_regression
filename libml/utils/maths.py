def mean_squared_error(p0, p1, X, y):
    cost = ((p0 + (p1 * X)) - y) * ((p0 + (p1 * X)) - y)
    return sum((1 / (2 * len(X))) * cost)


def normalize(array):
    minValue = min(array)
    maxValue = max(array)
    return (array - minValue) / (maxValue - minValue)

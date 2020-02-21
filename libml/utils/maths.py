def squared_error_cost(p0, p1, X, y):
    cost = ((p0 + (p1 * X)) - y) * ((p0 + (p1 * X)) - y)
    return (1 / (2 * len(X))) * cost

import matplotlib.pyplot as plt
import numpy as np


def plot_gradient_descent(X, y, p0, p1, i):
    plt.clf()
    plt.scatter(X, y)
    plt.plot(X, p0 + (p1 * X), "r--")
    plt.pause(0.01)

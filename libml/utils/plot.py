import matplotlib.pyplot as plt
import numpy as np


def plot_gradient_descent(X, y, p0, p1, cost):
    plt.clf()
    plt.subplot(2, 1, 1)
    plt.scatter(X, y)
    plt.plot(X, p0 + (p1 * X), "r--")
    plt.title('title')

    plt.subplot(2, 1, 2)
    plt.plot(cost, '.-')
    plt.title('mean_squared_error')

    plt.pause(0.01)

import numpy as np
from .utils.csv import read_csv
from .utils.maths import squared_error_cost
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 5.0)


class Trainer:
    def __init__(self, data_path=None, out_path=None, epochs=1000, lrate=0.001,
                 plot=False):
        """Trainer Model"""
        self.data_path = data_path
        self.out = out_path
        self.epochs = epochs
        self.lrate = lrate
        self.plot = plot
        self.data = read_csv(self.data_path)

    def gradient_descent(self):
        p0 = np.float32(0.0)
        p1 = np.float32(0.0)

        X = self.data.iloc[:, 0].to_numpy(dtype=np.float32)
        y = self.data.iloc[:, 1].to_numpy(dtype=np.float32)

        if (self.plot):
            plt.scatter(X, y)
            plt.show()

        m = np.float32(len(X))
        d = np.float32(1.0 / m)
        lrate = np.float32(self.lrate)

        for i in range(self.epochs):
            hyp = p0 + (X * p1)
            tmp0 = p0 - lrate * (d * sum(hyp - y))
            tmp1 = p1 - lrate * (d * sum((hyp - y) * X))
            p0 = tmp0
            p1 = tmp1

        print(hyp, p0, p1)

    def save():
        pass

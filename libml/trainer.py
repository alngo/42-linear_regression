import numpy as np
from .utils.csv import read_csv, write_csv
from .utils.plot import plot_gradient_descent
from .utils.maths import mean_squared_error, normalize
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 5.0)


class Trainer:
    def __init__(self, data_path=None, out_path=None, epochs=1000, lrate=0.5,
                 verbose=False, plot=False):
        """Trainer Model"""
        self.data_path = data_path
        self.out = out_path
        self.epochs = epochs
        self.lrate = lrate
        self.plot = plot
        self.verbose = verbose
        self.data = read_csv(self.data_path)

    def gradient_descent(self):
        p0 = np.float32(0.0)
        p1 = np.float32(0.0)
        cost = []

        [X, Xmin, Xmax] = normalize(
            self.data.iloc[:, 0].to_numpy(dtype=np.float32))
        [y, ymin, ymax] = normalize(
            self.data.iloc[:, 1].to_numpy(dtype=np.float32))

        m = np.float32(len(X))
        d = np.float32(1.0 / m)
        lrate = np.float32(self.lrate)

        for i in range(self.epochs):
            hyp = p0 + (X * p1)
            tmp0 = p0 - lrate * (d * sum(hyp - y))
            tmp1 = p1 - lrate * (d * sum((hyp - y) * X))
            p0 = tmp0
            p1 = tmp1
            cost.append(mean_squared_error(p0, p1, X, y))
            print(f"theta0: {p0} - theta1: {p1}")
            if (self.plot):
                plot_gradient_descent(X, y, p0, p1, cost)
        if (self.plot):
            plt.show()

        print(f"Mean squared error: {mean_squared_error(p0, p1, X, y)}")

        data = {'theta0': p0, 'theta1': p1,
                'Xmin': Xmin, 'Xmax': Xmax,
                'ymin': ymin, 'ymax': ymax, }

        write_csv(data=data, output=self.out)

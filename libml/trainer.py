# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainer.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:43:48 by alngo             #+#    #+#              #
#    Updated: 2020/03/02 10:19:17 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
from .utils.csv import read_csv, write_csv, check_csv
from .utils.plot import plot_gradient_descent
from .utils.maths import mean_squared_error, normalize, denormalize_theta
import matplotlib.pyplot as plt


class Trainer:
    def __init__(self, data_path=None, out_path=None, epochs=1000, lrate=0.5,
                 plot=False):
        """Trainer Model"""
        self.data_path = data_path
        self.out = out_path
        self.epochs = epochs
        self.lrate = lrate
        if lrate < 0 or lrate > 1:
            print(f"Invalid learning rate: expect a value between 0 and 1")
            sys.exit(1)
        self.plot = plot
        self.data = read_csv(self.data_path)


    @check_csv('km', 'price')
    def gradient_descent(self):
        p0 = np.float32(0.0)
        p1 = np.float32(0.0)
        cost = []
        p0_array = []
        p1_array = []

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
            p0_array.append(p0)
            p1_array.append(p1)
            cost.append(mean_squared_error(p0, p1, X, y))
            print(f"theta0: {p0} - theta1: {p1}")

        print(f"Mean squared error: {mean_squared_error(p0, p1, X, y)}")

        p0, p1 = denormalize_theta(self.data, X, p0, p1, ymin, ymax)

        data = {'theta0': p0, 'theta1': p1}

        if (self.out):
            write_csv(data=data, output=self.out)

        if (self.plot):
            plot_gradient_descent(X, y, p0_array, p1_array, cost)

        return data

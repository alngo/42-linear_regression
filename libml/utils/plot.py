# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:45:14 by alngo             #+#    #+#              #
#    Updated: 2020/02/24 09:45:33 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import numpy as np


def plot_gradient_descent(X, y, p0, p1, cost):
    plt.rcParams['figure.figsize'] = (10.0, 5.0)

    for i in range(len(cost)):
        plt.clf()
        plt.subplot(1, 2, 1)
        plt.scatter(X, y, label="data")
        plt.plot(X, p0[i] + (p1[i] * X), "r--", label="hypothesis")
        plt.title('Gradient descent')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(cost[0 : i], '.-', label="mean squared error", color='m')
        plt.title('Cost function')
        plt.legend()

        plt.pause(0.0001)

    plt.show()

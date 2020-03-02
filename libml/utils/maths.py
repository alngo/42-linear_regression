# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maths.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:45:07 by alngo             #+#    #+#              #
#    Updated: 2020/03/02 10:16:00 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys

def mean_squared_error(p0, p1, X, y):
    cost = ((p0 + (p1 * X)) - y) * ((p0 + (p1 * X)) - y)
    return sum((1 / (2 * len(X))) * cost)


def normalize(list):
    minValue = min(list)
    maxValue = max(list)
    newList = (list - minValue) / (maxValue - minValue)
    return [newList, minValue, maxValue]

def denormalize_theta(dataset, normalized_dataset, theta0, theta1, min, max):
    x0 = dataset.iloc[0, 0]
    x1 = dataset.iloc[1, 0]
    y0 = dataset.iloc[0, 1]
    nx0 = normalized_dataset[0]
    nx1 = normalized_dataset[1]
    hy0 = theta0 + (nx0 * theta1)
    hy1 = theta0 + (nx1 * theta1)

    p0 = (x1 / (x1 - x0)) * upscale(hy0, min, max) - (x0 / x1 * upscale(hy1, min, max))
    p1 = (y0 - p0) / x0


    print(f"x0: {x0}, x1: {x1}")
    print(f"x0n: {nx0}, x1n: {nx1}")
    print(f"y0n: {hy0}, y1n: {hy1}")
    print(f"y0: {y0}")
    print(f"{dataset}")
    print(f"{p0} - {p1}")
    return p0, p1


def scale(value, min, max):
    if min == 0 and max == 0:
        return np.float(0.0)
    return np.float64((value - min) / (max - min))


def upscale(value, min, max):
    return np.float64((value * (max - min)) + min)

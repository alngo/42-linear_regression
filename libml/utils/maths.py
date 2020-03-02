# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maths.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:45:07 by alngo             #+#    #+#              #
#    Updated: 2020/03/02 11:25:39 by alngo            ###   ########.fr        #
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

    try:
        p0 = (x1 / (x1 - x0)) * (upscale(hy0, min, max) - (x0 / x1 * upscale(hy1, min, max)))
        p1 = (y0 - p0) / x0
    except ZeroDivisionError:
        print(f'Zero division error')
        sys.exit(1)
    return p0, p1


def scale(value, min, max):
    try:
        res = np.float64((value - min) / (max - min))
    except ZeroDivisionError:
        print(f'Zero division error')
        sys.exit(1)
    return res


def upscale(value, min, max):
    return np.float64((value * (max - min)) + min)

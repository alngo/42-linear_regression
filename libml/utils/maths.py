# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maths.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:45:07 by alngo             #+#    #+#              #
#    Updated: 2020/02/25 13:02:01 by alngo            ###   ########.fr        #
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


def scale(value, min, max):
    if min == 0 and max == 0:
        return np.float(0.0)
    return np.float64((value - min) / (max - min))


def upscale(value, min, max):
    return np.float64((value * (max - min)) + min)

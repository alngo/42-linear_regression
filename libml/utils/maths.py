# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maths.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:45:07 by alngo             #+#    #+#              #
#    Updated: 2020/02/25 14:53:27 by alngo            ###   ########.fr        #
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
    res = 0.0
    try:
        res = np.float64((value - min) / (max - min))
    except ZeroDivisionError:
        print("Zero division error")
    except:
        return res


def upscale(value, min, max):
    print(value)
    print(min)
    print(max)
    return np.float64((value * (max - min)) + min)

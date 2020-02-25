# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maths.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:45:07 by alngo             #+#    #+#              #
#    Updated: 2020/02/25 15:17:43 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def mean_squared_error(p0, p1, X, y):
    cost = ((p0 + (p1 * X)) - y) * ((p0 + (p1 * X)) - y)
    return sum((1 / (2 * len(X))) * cost)


def normalize(list):
    minValue = min(list)
    maxValue = max(list)
    try:
        newList = (list - minValue) / (maxValue - minValue)
    except:
        return [list, minValue, maxValue]
    return [newList, minValue, maxValue]


def scale(value, min, max):
    try:
        return (value - min) / (max - min)
    except:
        return value


def upscale(value, min, max):
    return (value * (max - min)) + min

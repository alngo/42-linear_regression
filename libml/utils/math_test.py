# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math_test.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 10:00:58 by alngo             #+#    #+#              #
#    Updated: 2020/02/24 10:10:06 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .maths import mean_squared_error, normalize, scale, upscale
import numpy as np


def test_scale_function():
    assert scale(5, 0, 10) == 0.5


def test_upscale_function():
    assert upscale(0.5, 0, 10) == 5


def test_normalize_function():
    lst = np.array([0,1,2,3,4,5,6,7,8,9,10])
    [nlst, nMin, nMax] = normalize(lst)
    assert nMin == 0
    assert nMax == 10
    assert nlst[0] == 0
    assert nlst[1] == 0.1
    assert nlst[2] == 0.2
    assert nlst[3] == 0.3
    assert nlst[4] == 0.4
    assert nlst[5] == 0.5
    assert nlst[6] == 0.6
    assert nlst[7] == 0.7
    assert nlst[8] == 0.8
    assert nlst[9] == 0.9
    assert nlst[10] == 1


def test_mean_squared_error_function():
    X = np.array([0,1,2,3,4,5])
    y = np.array([0,1,2,3,4,5])
    cost = mean_squared_error(0, 1, X, y)
    assert cost == 0

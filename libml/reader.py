# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reader.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:44:24 by alngo             #+#    #+#              #
#    Updated: 2020/03/02 09:22:01 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .utils.csv import read_csv, check_csv
from .utils.maths import scale, upscale
import numpy as np


class Reader:
    def __init__(self, *args, path=None):
        """Reader Model"""
        self.args = args
        self.path = path
        self.data = read_csv(self.path)


    @check_csv('theta0', 'theta1')
    def linear_regression(self):
        m = self.args[0]
        p0 = np.float64(self.data['theta0'][0])
        p1 = np.float64(self.data['theta1'][0])
        prediction = p0 + (m * p1)
        return int(prediction)

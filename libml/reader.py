# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reader.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:44:24 by alngo             #+#    #+#              #
#    Updated: 2020/02/24 09:44:25 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .utils.csv import read_csv
from .utils.maths import scale, upscale
import numpy as np


class Reader:
    def __init__(self, *args, path=None):
        """Reader Model"""
        self.args = args
        self.path = path
        self.df = read_csv(self.path)

    def linear_regression(self):
        m = scale(self.args[0], self.df['Xmin'], self.df['Xmax'])
        p0 = np.float64(self.df['theta0'][0])
        p1 = np.float64(self.df['theta1'][0])
        prediction = p0 + (m * p1)
        return int(upscale(prediction, self.df['ymin'], self.df['ymax']))

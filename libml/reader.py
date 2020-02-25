# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reader.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:44:24 by alngo             #+#    #+#              #
#    Updated: 2020/02/25 15:15:04 by alngo            ###   ########.fr        #
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


    @check_csv('theta0', 'theta1', 'Xmin', 'Xmax', 'ymin', 'ymax')
    def linear_regression(self):
        mileage = self.args[0]
        p0 = np.float(self.data['theta0'][0])
        p1 = np.float(self.data['theta1'][0])
        Xmin = np.float(self.data['Xmin'][0])
        Xmax = np.float(self.data['Xmax'][0])
        ymin = np.float(self.data['ymin'][0])
        ymax = np.float(self.data['ymax'][0])

        m = scale(mileage, Xmin, Xmax)
        predict = p0 + (m * p1)
        return int(upscale(predict, ymin, ymax))

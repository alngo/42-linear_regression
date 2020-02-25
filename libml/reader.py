# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reader.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:44:24 by alngo             #+#    #+#              #
#    Updated: 2020/02/25 13:03:10 by alngo            ###   ########.fr        #
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
        m = scale(self.args[0], self.data['Xmin'][0], self.data['Xmax'][0])
        p0 = np.float64(self.data['theta0'][0])
        p1 = np.float64(self.data['theta1'][0])
        if m == 0.0 and p0 == 0.0 and p1 == 0.0:
            return "Error"
        prediction = p0 + (m * p1)
        if prediction:
            return int(upscale(prediction, self.data['ymin'][0],
                self.data['ymax'][0]))
        else:
            return 0



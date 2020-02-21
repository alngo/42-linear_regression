import pandas as pd
from .utils.csv import get_parameters
import sys


class Reader:
    def __init__(self, *args, path=None):
        """Reader Model"""
        self.args = args
        self.path = path
        self.parameters = get_parameters(self.path)

    def linear_regression(self):
        m = self.args[0]
        p0 = int(self.parameters[0])
        p1 = int(self.parameters[1])
        return p0 + m * p1

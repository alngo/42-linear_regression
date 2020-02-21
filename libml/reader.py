import pandas as pd
from utils.csv import get_parameters
import sys


class Reader:
    def __init__(self, *args, path=None):
        self.args = args
        self.path = path
        self.parameters = get_parameters(self.path)
        print(f"{self.parameters}")


# def linear_regression(mileage, path="./models/model.csv"):

import pandas as pd
import sys


def get_parameters(path):
    parameters = None
    try:
        parameters = pd.read_csv(path, sep=',')
    except FileNotFoundError:
        print(f'File at path: "{path}" not found')
        sys.exit()
    except:
        print(f'An unexpected error occured on read_csv')
        sys.exit()
    return parameters.columns.tolist()


class Reader:
    def __init__(self, *args, path=None):
        self.args = args
        self.path = path
        self.parameters = get_parameters(self.path)
        print(f"{self.parameters}")


# def linear_regression(mileage, path="./models/model.csv"):

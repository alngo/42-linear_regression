from .utils.csv import read_csv


class Reader:
    def __init__(self, *args, path=None):
        """Reader Model"""
        self.args = args
        self.path = path
        self.parameters = read_csv(self.path).columns.tolist()

    def linear_regression(self):
        m = self.args[0]
        p0 = int(self.parameters[0])
        p1 = int(self.parameters[1])
        return p0 + m * p1

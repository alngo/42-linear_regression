from .utils.csv import get_parameters


class Reader:
    def __init__(self, data_path=None, out_path=None, plot=False):
        """Trainer Model"""
        self.data_path = data_path
        self.out = out_path
        self.data = get_parameters(self.data_path)

    def gradient_descent(self):
        pass


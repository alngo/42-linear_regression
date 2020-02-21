import pandas as pd
import sys


def get_parameters(path):
    parameters = None
    try:
        parameters = pd.read_csv(path, sep=',')
    except FileNotFoundError:
        print(f'File at path: "{path}" not found')
        sys.exit(1)
    except:
        print(f'An unexpected error occured on read_csv')
        sys.exit(1)
    return parameters.columns.tolist()

import pandas as pd
import sys


def read_csv(path):
    parameters = None
    try:
        parameters = pd.read_csv(path, sep=',')
    except FileNotFoundError:
        print(f'File at path: "{path}" not found')
        sys.exit(1)
    except:
        print(f'An unexpected error occured on read_csv')
        sys.exit(1)
    return parameters


def write_csv(array):
    try:
        print(f"{array}")
        df = pd.dataframe(columns=array)
    except:
        print(f'An unexpected error occured on write_csv')
        sys.exit(1)

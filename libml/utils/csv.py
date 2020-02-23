import pandas as pd
import sys


def read_csv(path):
    parameters = None
    try:
        parameters = pd.read_csv(path)
    except FileNotFoundError:
        print(f'File at path: "{path}" not found')
        sys.exit(1)
    except:
        print(f'An unexpected error occured on read_csv')
        sys.exit(1)
    return parameters


def write_csv(data, output):
    df = pd.DataFrame(data=data, index=[0])
    df.to_csv(output, index=None)

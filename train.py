import argparse
from libml.trainer import Trainer


def arguments():
    parser = argparse.ArgumentParser(
        description='Train a model given a dataset')

    parser.add_argument('--path', dest="path", metavar='path',
                        help='must be a valid dataset path')
    parser.add_argument('--out', dest="out", metavar='path',
                        help='must be a valid output path')
    parser.add_argument('--plot', dest="plot", default=False, type=bool,
                        help='visual mode')
    args = parser.parse_args()
    return args


def predict():
    path = "./datasets/data.csv"
    out = "./models/model.csv"
    plot = False
    if args.path is not None:
        path = args.path
    if args.out is not None:
        out = args.out
    if args.plot is not False:
        plot = args.plot
    train = Trainer(data_path=path, out_path=out, plot=plot)
    train.gradient_descent()


if __name__ == "__main__":
    predict()

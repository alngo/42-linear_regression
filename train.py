# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:43:41 by alngo             #+#    #+#              #
#    Updated: 2020/02/24 09:43:42 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
                        help='plot training')
    parser.add_argument('--epochs', dest="epochs", type=int,
                        help='number of iteration')
    parser.add_argument('--lrate', dest="lrate", type=float,
                        help='number of iteration')
    args = parser.parse_args()
    return args


def train():
    path = "./datasets/data.csv"
    out = "./models/model.csv"
    plot = False
    verbose = False
    lrate = 0.5
    epochs = 1000
    args = arguments()

    if args.path is not None:
        path = args.path
    if args.out is not None:
        out = args.out
    if args.lrate is not None:
        lrate = args.lrate
    if args.epochs is not None:
        epochs = args.epochs
    if args.plot is not False:
        plot = True

    train = Trainer(data_path=path, out_path=out, epochs=epochs, lrate=lrate,
                    verbose=verbose, plot=plot)

    train.gradient_descent()


if __name__ == "__main__":
    train()

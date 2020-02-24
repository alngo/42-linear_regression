# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:44:15 by alngo             #+#    #+#              #
#    Updated: 2020/02/24 09:44:16 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from libml.reader import Reader


def arguments():
    parser = argparse.ArgumentParser(
        description='Predict the price given an mileage')

    parser.add_argument('--path', dest="path", metavar='path',
                        help='must be a valid model.csv path')
    parser.add_argument('-p', dest="path", metavar='path',
                        help='must be a valid model.csv path')
    parser.add_argument('mileage', metavar='<mileage>',
                        type=int,  help='must be a valid integer')
    args = parser.parse_args()
    return args


def predict():

    path = "./models/model.csv"
    args = arguments()
    if args.path is not None:
        path = args.path
    read = Reader(args.mileage, path=path)
    prediction = read.linear_regression()
    print(f"Estimated price: {prediction}")


if __name__ == "__main__":
    predict()

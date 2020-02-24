# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reader_test.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:44:30 by alngo             #+#    #+#              #
#    Updated: 2020/02/24 09:44:31 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .reader import Reader


def test_reader_init():
    path = "./models/test.csv"
    r = Reader(1, path=path)
    assert r.args[0] == 1
    assert r.path == path
    assert r.df['theta0'][0] == 0
    assert r.df['theta1'][0] == 2


def test_reader_linear_regression():
    r = Reader(1, path="./models/test.csv")
    predicted = r.linear_regression()
    assert predicted == 2

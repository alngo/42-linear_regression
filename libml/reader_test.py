# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reader_test.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 09:44:30 by alngo             #+#    #+#              #
#    Updated: 2020/03/02 11:19:59 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .reader import Reader
import pytest


def test_reader_init():
    path = "./models/test.csv"
    r = Reader(1, path=path)
    assert r.args[0] == 1
    assert r.path == path
    assert r.data['theta0'][0] == 0
    assert r.data['theta1'][0] == 2


def test_trainer_invalid_init(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        path = "./models/invalid.csv"
        r = Reader(path=path)
        r.linear_regression()
    captured = capsys.readouterr()
    assert captured.out == "Can't process linear_regression: invalid csv\n"
    assert pytest_wrapped_e.value.code == 1


def test_reader_linear_regression():
    r = Reader(1, path="./models/test.csv")
    predicted = r.linear_regression()
    assert predicted == 2

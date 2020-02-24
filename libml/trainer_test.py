# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainer_test.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 10:10:47 by alngo             #+#    #+#              #
#    Updated: 2020/02/24 11:11:03 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .trainer import Trainer
import pytest


def test_trainer_init():
    path = "./datasets/test.csv"
    t = Trainer(data_path=path, epochs=10, lrate=0.1, plot=True)
    assert t.data_path == path
    assert t.out == None
    assert t.epochs == 10
    assert t.lrate == 0.1
    assert t.plot == True


def test_trainer_invalid_init(capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        path = "./datasets/invalid.csv"
        t = Trainer(data_path=path, epochs=10, lrate=0.1, plot=True)
        t.gradient_descent()
    captured = capsys.readouterr()
    assert captured.out == "Can't process gradient_descent: invalid csv\n"
    assert pytest_wrapped_e.value.code == 1


def test_trainer_gradient_descent():
    path = "./datasets/test.csv"
    t = Trainer(data_path=path, epochs=1000, lrate=0.1, plot=False)
    data = t.gradient_descent()


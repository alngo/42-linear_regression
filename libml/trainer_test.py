# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainer_test.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alngo <alngo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 10:10:47 by alngo             #+#    #+#              #
#    Updated: 2020/02/24 10:20:25 by alngo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .trainer import Trainer


def test_trainer_init():
    path = "./datasets/test.csv"
    t = Trainer(data_path=path, epochs=10, lrate=0.1, plot=True)
    assert t.data_path == path
    assert t.out == None
    assert t.epochs == 10
    assert t.lrate == 0.1
    assert t.plot == True


def test_trainer_gradient_descent():
    path = "./datasets/test.csv"
    t = Trainer(data_path=path, epochs=1000, lrate=0.1, plot=False)
    data = t.gradient_descent()

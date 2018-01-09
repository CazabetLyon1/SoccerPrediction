# -*- coding: utf-8 -*-

from sklearn.svm import LinearSVC
from Utils import *


model = LinearSVC()
model.fit(x_train, y_train)


def linearfulltimeresult(home, away):
    w = winner(home, away, model)
    return fulltimeresult(home, away, w)


def linearprecision():
    return precision(model)

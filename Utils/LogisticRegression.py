# -*- coding: utf-8 -*-

from sklearn.linear_model import LogisticRegression
from Utils import *


model = LogisticRegression()
model.fit(x_train, y_train)


def logisticfulltimeresult(home, away):
    w = winner(home, away, model)
    return fulltimeresult(home, away, w)


def logisticprecision():
    return precision(model)

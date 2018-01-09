# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestClassifier
from Utils import *


model = RandomForestClassifier()
model.fit(x_train, y_train)


def rfulltimeresult(home, away):
    w = winner(home, away, model)
    return fulltimeresult(home, away, w)


def rprecision():
    return precision(model)

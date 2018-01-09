# -*- coding: utf-8 -*-

from FileRead import *
from sklearn.metrics import accuracy_score


"""Fontion pour fusionner deux dictionnaires"""


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


"""Données d'entrainement"""

x_train = traindata[['HAS', 'HDS', 'HSTM', 'HSM', 'AAS', 'ADS', 'ASTM', 'ASM']]
y_train = traindata['Result']

dico1 = predictdict()
dico2 = trainingdict()
dico3 = merged()
dico4 = merge_two_dicts(dico1, dico2)
dico = merge_two_dicts(dico4, dico3)


"""Fonction qui détermine le vainqueur avec la différence probable de buts."""


def winner(home, away, m):
    domicile = dico[home]["MoyennesH"]
    exterieur = dico[away]["MoyennesA"]

    """Données d'entrainement"""
    train = [domicile + exterieur]

    prediction = m.predict(train)
    diff = prediction[0]

    if diff > 0:
        return [diff, 'H']
    elif prediction[0] < 0:
        return [diff, 'A']
    else:
        return [diff, 'D']


def fulltimeresult(home, away, w):
    if w[1] == 'H':
        chaine = "" + home + " gagne avec {} but(s) de différence".format(w[0])
        return chaine
    elif w[1] == 'A':
        chaine = "" + away + " gagne avec {} but(s) de différence".format(w[0] * -1)
        return chaine
    else:
        chaine = "" + home + " Vs " + away + " match nul probable"
        return chaine


def precision(m):
    result1 = []
    result2 = []
    for j in range(len(predictdata.FTR)):
        r2 = winner(predictdata.loc[j, "HomeTeam"], predictdata.loc[j, "AwayTeam"], m)
        result2.append(r2[1])

    for j in range(len(traindata.FTR)):
        r1 = winner(traindata.loc[j, "HomeTeam"], traindata.loc[j, "AwayTeam"], m)
        result1.append(r1[1])

    result = result1 + result2
    real = traindata["FTR"].tolist() + predictdata["FTR"].tolist()
    accuracy = accuracy_score(real, result) * 100
    print("Précision de la loi {}: {:.2f}%".format(m, accuracy))

    return accuracy

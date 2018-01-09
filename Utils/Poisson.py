# -*- coding: utf-8 -*-

from FileRead import *
from scipy.stats import poisson
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.metrics as skm

dico = merged()


def exception(home, away):
    equipes = set(predictdata.HomeTeam)
    if home not in equipes:
        raise NameError(home + " ne joue pas en " + trainfile)
    if away not in equipes:
        raise NameError(away + " ne joue pas en " + trainfile)


def butsprobablesdomicile(home, away):
    n = dico[home]["AttaqueHome"] * dico[away]["DefenseAway"] * float(data.HomeGoals.mean())
    return n


def butsprobablesexterieur(home, away):
    n = dico[away]["AttaqueAway"] * dico[home]["DefenseHome"] * float(data.AwayGoals.mean())
    return n


def possibilities(home, away):
    p1 = []
    p2 = []
    for j in range(10):
        p1.append(poisson.pmf(j, butsprobablesdomicile(home, away)))
        p2.append(poisson.pmf(j, butsprobablesexterieur(home, away)))

    p = []

    for value1 in p1:
        liste = []
        for value2 in p2:
            liste.append(value1*value2)
        p.append(liste)

    return p


def resultgraph(home, away):
    mylist = possibilities(home, away)
    sns.heatmap(mylist)
    plt.title("Matrice des differentes possibilites!")
    plt.xlabel(away)
    plt.ylabel(home)
    plt.show()


def winner(home, away):
    mylist = possibilities(home, away)

    tabhomewin = []
    tabawaywin = []
    tabdraw = []
    for h in range(len(mylist)):
        for a in range(len(mylist)):
            if h > a:
                tabhomewin.append(mylist[h][a])
            elif h < a:
                tabawaywin.append(mylist[h][a])
            else:
                tabdraw.append(mylist[h][a])

    homewin = sum(tabhomewin)*100
    awaywin = sum(tabawaywin)*100
    draw = sum(tabdraw)*100

    w = max(max(homewin, awaywin), draw)

    if w == homewin:
        return [homewin, 'H']
    elif w == awaywin:
        return [awaywin, 'A']
    else:
        return [draw, 'D']


def pfulltimeresult(home, away):
    exception(home, away)
    w = winner(home, away)
    if w[1] == 'H':
        chaine = "" + home + " a {:.2f}% de chances de gagner".format(w[0])
        return chaine
    elif w[1] == 'A':
        chaine = "" + away + " a {:.2f}% de chances de gagner".format(w[0] * -1)
        return chaine
    else:
        chaine = "Il y a {:.2f}% de chances d'avoir un match nul".format(w[0])
        return chaine


def pprecision():
    result = []
    for j in range(len(traindata.FTR)):
        r = winner(traindata.loc[j, "HomeTeam"], traindata.loc[j, "AwayTeam"])
        result.append(r[1])

    accuracy = skm.accuracy_score(traindata["FTR"], result) * 100
    print("Précision de la loi poisson: {:.2f}%".format(accuracy))

    return accuracy

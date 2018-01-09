# -*- coding: utf-8 -*-

import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fonction", type=str, help="Appeler une fonction particulière!")
parser.add_argument("trainfile", type=str, default="Ligue1.csv")
parser.add_argument("domicile", type=str, help="Equipe à domicile")
parser.add_argument("exterieur", type=str, help="Equipe à l'extérieur")
args = parser.parse_args()

trainfile = args.trainfile

traindata = pd.read_csv(trainfile+".csv")
traindata = traindata[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HST', 'AST', 'HS', 'AS', 'HTHG', 'HTAG']]
traindata = traindata.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
traindata = traindata.fillna(0)

predictdata = pd.read_csv(trainfile+"new.csv")
predictdata = predictdata[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HST', 'AST', 'HS', 'AS', 'HTHG', 'HTAG']]
predictdata = predictdata.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
predictdata = predictdata.fillna(0)

data = traindata.append(predictdata)


""" Création d'un dictionnaire contenant les performances de chaque équipe """


def trainingdict():
    trainingdico = dict()
    listeEquipes = set(traindata.HomeTeam)
    homeMean = float(traindata.HomeGoals.mean())
    awayMean = float(traindata.AwayGoals.mean())
    homeShotTargetMean = float(traindata.HST.mean())
    awayShotTargetMean = float(traindata.AST.mean())
    homeShotMean = float(traindata.HS.mean())
    awayShotMean = float(traindata.AS.mean())
    for team in listeEquipes:
        nbHomeGoals = sum(traindata.HomeGoals[traindata.HomeTeam == team])
        nbAwayGoals = sum(traindata.AwayGoals[traindata.AwayTeam == team])
        nbHomeTaken = sum(traindata.AwayGoals[traindata.HomeTeam == team])
        nbAwayTaken = sum(traindata.HomeGoals[traindata.AwayTeam == team])
        nbHomeShotsTarget = sum(traindata.HST[traindata.HomeTeam == team])
        nbAwayShotsTarget = sum(traindata.AST[traindata.AwayTeam == team])
        nbHomeShots = sum(traindata.HS[traindata.HomeTeam == team])
        nbAwayShots = sum(traindata.AS[traindata.AwayTeam == team])
        nbHomeGames = len(traindata[traindata.HomeTeam == team])
        nbAwayGames = len(traindata[traindata.AwayTeam == team])
        homeAttackStrength = float(float(nbHomeGoals) / float(nbHomeGames) / homeMean)
        awayAttackStrength = float(float(nbAwayGoals) / float(nbAwayGames) / awayMean)
        homeDefenseStrength = float(float(nbHomeTaken) / float(nbHomeGames) / awayMean)
        awayDefenseStrength = float(float(nbAwayTaken) / float(nbAwayGames) / homeMean)
        homeShotTargetStrength = float(float(nbHomeShotsTarget) / float(nbHomeGames) / homeShotTargetMean)
        homeShotStrength = float(float(nbHomeShots) / float(nbHomeGames) / homeShotMean)
        awayShotTargetStrength = float(float(nbAwayShotsTarget) / float(nbAwayGames) / awayShotTargetMean)
        awayShotStrength = float(float(nbAwayShots) / float(nbAwayGames) / awayShotMean)
        trainingdico[team] = {"ButsHome": nbHomeGoals, "ButsAway": nbAwayGoals, "MatchsHome": nbHomeGames,
                              "MatchsAway": nbAwayGames, "AttaqueHome": homeAttackStrength,
                              "AttaqueAway": awayAttackStrength, "DefenseHome": homeDefenseStrength,
                              "HomeShotTarget": homeShotTargetStrength, "HomeShot": homeShotStrength,
                              "AwayShotTarget": awayShotTargetStrength, "AwayShot": awayShotStrength,
                              "DefenseAway": awayDefenseStrength, "MoyennesH": [homeAttackStrength, homeDefenseStrength,
                                                                                homeShotTargetStrength,
                                                                                homeShotStrength],
                              "MoyennesA": [awayAttackStrength, awayDefenseStrength, awayShotTargetStrength,
                                            awayShotStrength]}


def trainingdict():
    trainingdico = dict()
    listeEquipes = set(traindata.HomeTeam)
    homeMean = float(traindata.HomeGoals.mean())
    awayMean = float(traindata.AwayGoals.mean())
    homeShotTargetMean = float(traindata.HST.mean())
    awayShotTargetMean = float(traindata.AST.mean())
    homeShotMean = float(traindata.HS.mean())
    awayShotMean = float(traindata.AS.mean())
    for team in listeEquipes:
        nbHomeGoals = sum(traindata.HomeGoals[traindata.HomeTeam == team])
        nbAwayGoals = sum(traindata.AwayGoals[traindata.AwayTeam == team])
        nbHomeTaken = sum(traindata.AwayGoals[traindata.HomeTeam == team])
        nbAwayTaken = sum(traindata.HomeGoals[traindata.AwayTeam == team])
        nbHomeShotsTarget = sum(traindata.HST[traindata.HomeTeam == team])
        nbAwayShotsTarget = sum(traindata.AST[traindata.AwayTeam == team])
        nbHomeShots = sum(traindata.HS[traindata.HomeTeam == team])
        nbAwayShots = sum(traindata.AS[traindata.AwayTeam == team])
        nbHomeGames = len(traindata[traindata.HomeTeam == team])
        nbAwayGames = len(traindata[traindata.AwayTeam == team])
        homeAttackStrength = float(float(nbHomeGoals) / float(nbHomeGames) / homeMean)
        awayAttackStrength = float(float(nbAwayGoals) / float(nbAwayGames) / awayMean)
        homeDefenseStrength = float(float(nbHomeTaken) / float(nbHomeGames) / awayMean)
        awayDefenseStrength = float(float(nbAwayTaken) / float(nbAwayGames) / homeMean)
        homeShotTargetStrength = float(float(nbHomeShotsTarget) / float(nbHomeGames) / homeShotTargetMean)
        homeShotStrength = float(float(nbHomeShots) / float(nbHomeGames) / homeShotMean)
        awayShotTargetStrength = float(float(nbAwayShotsTarget) / float(nbAwayGames) / awayShotTargetMean)
        awayShotStrength = float(float(nbAwayShots) / float(nbAwayGames) / awayShotMean)
        trainingdico[team] = {"ButsHome": nbHomeGoals, "ButsAway": nbAwayGoals, "MatchsHome": nbHomeGames,
                              "MatchsAway": nbAwayGames, "AttaqueHome": homeAttackStrength,
                              "AttaqueAway": awayAttackStrength, "DefenseHome": homeDefenseStrength,
                              "HomeShotTarget": homeShotTargetStrength, "HomeShot": homeShotStrength,
                              "AwayShotTarget": awayShotTargetStrength, "AwayShot": awayShotStrength,
                              "DefenseAway": awayDefenseStrength, "MoyennesH": [homeAttackStrength, homeDefenseStrength,
                                                                                homeShotTargetStrength,
                                                                                homeShotStrength],
                              "MoyennesA": [awayAttackStrength, awayDefenseStrength, awayShotTargetStrength,
                                            awayShotStrength]}

    return trainingdico


def predictdict():
    predictingdico = dict()
    listeEquipes = set(predictdata.HomeTeam)
    homeMean = float(predictdata.HomeGoals.mean())
    awayMean = float(predictdata.AwayGoals.mean())
    homeShotTargetMean = float(predictdata.HST.mean())
    awayShotTargetMean = float(predictdata.AST.mean())
    homeShotMean = float(predictdata.HS.mean())
    awayShotMean = float(predictdata.AS.mean())
    for team in listeEquipes:
        nbHomeGoals = sum(predictdata.HomeGoals[predictdata.HomeTeam == team])
        nbAwayGoals = sum(predictdata.AwayGoals[predictdata.AwayTeam == team])
        nbHomeTaken = sum(predictdata.AwayGoals[predictdata.HomeTeam == team])
        nbAwayTaken = sum(predictdata.HomeGoals[predictdata.AwayTeam == team])
        nbHomeShotsTarget = sum(predictdata.HST[predictdata.HomeTeam == team])
        nbAwayShotsTarget = sum(predictdata.AST[predictdata.AwayTeam == team])
        nbHomeShots = sum(predictdata.HS[predictdata.HomeTeam == team])
        nbAwayShots = sum(predictdata.AS[predictdata.AwayTeam == team])
        nbHomeGames = len(predictdata[predictdata.HomeTeam == team])
        nbAwayGames = len(predictdata[predictdata.AwayTeam == team])
        homeAttackStrength = float(float(nbHomeGoals) / float(nbHomeGames) / homeMean)
        awayAttackStrength = float(float(nbAwayGoals) / float(nbAwayGames) / awayMean)
        homeDefenseStrength = float(float(nbHomeTaken) / float(nbHomeGames) / awayMean)
        awayDefenseStrength = float(float(nbAwayTaken) / float(nbAwayGames) / homeMean)
        homeShotTargetStrength = float(float(nbHomeShotsTarget) / float(nbHomeGames) / homeShotTargetMean)
        homeShotStrength = float(float(nbHomeShots) / float(nbHomeGames) / homeShotMean)
        awayShotTargetStrength = float(float(nbAwayShotsTarget) / float(nbAwayGames) / awayShotTargetMean)
        awayShotStrength = float(float(nbAwayShots) / float(nbAwayGames) / awayShotMean)
        predictingdico[team] = {"ButsHome": nbHomeGoals, "ButsAway": nbAwayGoals, "MatchsHome": nbHomeGames,
                                "MatchsAway": nbAwayGames, "AttaqueHome": homeAttackStrength,
                                "AttaqueAway": awayAttackStrength, "DefenseHome": homeDefenseStrength,
                                "HomeShotTarget": homeShotTargetStrength, "HomeShot": homeShotStrength,
                                "AwayShotTarget": awayShotTargetStrength, "AwayShot": awayShotStrength,
                                "DefenseAway": awayDefenseStrength, "MoyennesH": [homeAttackStrength,
                                                                                  homeDefenseStrength,
                                                                                  homeShotTargetStrength,
                                                                                  homeShotStrength],
                                "MoyennesA": [awayAttackStrength, awayDefenseStrength, awayShotTargetStrength,
                                              awayShotStrength]}

    return predictingdico


def merged():
    mergdico = dict()
    listeEquipes = set(data.HomeTeam)
    homeMean = float(data.HomeGoals.mean())
    awayMean = float(data.AwayGoals.mean())
    homeShotTargetMean = float(data.HST.mean())
    awayShotTargetMean = float(data.AST.mean())
    homeShotMean = float(data.HS.mean())
    awayShotMean = float(data.AS.mean())
    for team in listeEquipes:
        nbHomeGoals = sum(data.HomeGoals[data.HomeTeam == team])
        nbAwayGoals = sum(data.AwayGoals[data.AwayTeam == team])
        nbHomeTaken = sum(data.AwayGoals[data.HomeTeam == team])
        nbAwayTaken = sum(data.HomeGoals[data.AwayTeam == team])
        nbHomeShotsTarget = sum(data.HST[data.HomeTeam == team])
        nbAwayShotsTarget = sum(data.AST[data.AwayTeam == team])
        nbHomeShots = sum(data.HS[data.HomeTeam == team])
        nbAwayShots = sum(data.AS[data.AwayTeam == team])
        nbHomeGames = len(data[data.HomeTeam == team])
        nbAwayGames = len(data[data.AwayTeam == team])
        homeAttackStrength = float(float(nbHomeGoals) / float(nbHomeGames) / homeMean)
        awayAttackStrength = float(float(nbAwayGoals) / float(nbAwayGames) / awayMean)
        homeDefenseStrength = float(float(nbHomeTaken) / float(nbHomeGames) / awayMean)
        awayDefenseStrength = float(float(nbAwayTaken) / float(nbAwayGames) / homeMean)
        homeShotTargetStrength = float(float(nbHomeShotsTarget) / float(nbHomeGames) / homeShotTargetMean)
        homeShotStrength = float(float(nbHomeShots) / float(nbHomeGames) / homeShotMean)
        awayShotTargetStrength = float(float(nbAwayShotsTarget) / float(nbAwayGames) / awayShotTargetMean)
        awayShotStrength = float(float(nbAwayShots) / float(nbAwayGames) / awayShotMean)
        mergdico[team] = {"ButsHome": nbHomeGoals, "ButsAway": nbAwayGoals, "MatchsHome": nbHomeGames,
                          "MatchsAway": nbAwayGames, "AttaqueHome": homeAttackStrength,
                          "AttaqueAway": awayAttackStrength, "DefenseHome": homeDefenseStrength,
                          "HomeShotTarget": homeShotTargetStrength, "HomeShot": homeShotStrength,
                          "AwayShotTarget": awayShotTargetStrength, "AwayShot": awayShotStrength,
                          "DefenseAway": awayDefenseStrength, "MoyennesH": [homeAttackStrength, homeDefenseStrength,
                                                                            homeShotTargetStrength, homeShotStrength],
                          "MoyennesA": [awayAttackStrength, awayDefenseStrength, awayShotTargetStrength,
                                        awayShotStrength]}

    return mergdico


HAS = []
HDS = []
AAS = []
ADS = []
HSTM = []
ASTM = []
HSM = []
ASM = []

tdico = trainingdict()
for i in range(len(traindata.HomeTeam)):
    HAS.append(tdico[traindata.loc[i, "HomeTeam"]]["AttaqueHome"])
    HDS.append(tdico[traindata.loc[i, "HomeTeam"]]["DefenseHome"])
    AAS.append(tdico[traindata.loc[i, "AwayTeam"]]["AttaqueAway"])
    ADS.append(tdico[traindata.loc[i, "AwayTeam"]]["DefenseAway"])
    HSTM.append(tdico[traindata.loc[i, "HomeTeam"]]["HomeShotTarget"])
    ASTM.append(tdico[traindata.loc[i, "AwayTeam"]]["AwayShotTarget"])
    HSM.append(tdico[traindata.loc[i, "HomeTeam"]]["HomeShot"])
    ASM.append(tdico[traindata.loc[i, "AwayTeam"]]["AwayShot"])

traindata['HAS'] = HAS
traindata['AAS'] = AAS
traindata['HDS'] = HDS
traindata['ADS'] = ADS
traindata['HSTM'] = HSTM
traindata['ASTM'] = ASTM
traindata['HSM'] = HSM
traindata['ASM'] = ASM

resultat = []
for i in range(len(traindata.HomeGoals)):
    resultat.append(traindata.loc[i, "HomeGoals"] - traindata.loc[i, "AwayGoals"])

traindata["Result"] = resultat


HAS1 = []
HDS1 = []
AAS1 = []
ADS1 = []
HSTM1 = []
ASTM1 = []
HSM1 = []
ASM1 = []

pdico = predictdict()
for i in range(len(predictdata.HomeTeam)):
    HAS1.append(pdico[predictdata.loc[i, "HomeTeam"]]["AttaqueHome"])
    HDS1.append(pdico[predictdata.loc[i, "HomeTeam"]]["DefenseHome"])
    AAS1.append(pdico[predictdata.loc[i, "AwayTeam"]]["AttaqueAway"])
    ADS1.append(pdico[predictdata.loc[i, "AwayTeam"]]["DefenseAway"])
    HSTM1.append(pdico[predictdata.loc[i, "HomeTeam"]]["HomeShotTarget"])
    ASTM1.append(pdico[predictdata.loc[i, "AwayTeam"]]["AwayShotTarget"])
    HSM1.append(pdico[predictdata.loc[i, "HomeTeam"]]["HomeShot"])
    ASM1.append(pdico[predictdata.loc[i, "AwayTeam"]]["AwayShot"])

predictdata['HAS'] = HAS1
predictdata['AAS'] = AAS1
predictdata['HDS'] = HDS1
predictdata['ADS'] = ADS1
predictdata['HSTM'] = HSTM1
predictdata['ASTM'] = ASTM1
predictdata['HSM'] = HSM1
predictdata['ASM'] = ASM1

resultat1 = []
for i in range(len(predictdata.HomeGoals)):
    resultat1.append(predictdata.loc[i, "HomeGoals"] - predictdata.loc[i, "AwayGoals"])
predictdata["Result"] = resultat1

HAS2 = []
HDS2 = []
AAS2 = []
ADS2 = []
HSTM2 = []
ASTM2 = []
HSM2 = []
ASM2 = []

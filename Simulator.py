# -*- coding: utf-8 -*-

from Utils.Poisson import *
from Utils.LineaRegression import *
from Utils.LogisticRegression import *
from Utils.RandomForest import *
from matplotlib import pyplot

home = args.domicile
away = args.exterieur
exception(home, away)
fonction = args.fonction


def main():
    if fonction == "butsprobables":
        n1 = butsprobablesdomicile(home, away)
        print("****************************************************************************************")
        print("  " + home + " est susceptible de marquer {} buts en moyenne dans ce match".format(n1))
        print("****************************************************************************************")
        n2 = butsprobablesexterieur(home, away)
        print("****************************************************************************************")
        print("  " + away + " est susceptible de marquer {} buts en moyenne dans ce match".format(n2))
        print("****************************************************************************************")
        liste = [n1, n2]
        pyplot.bar(range(2), liste, width=0.6, color='green',
                   edgecolor='red', linewidth=2, yerr=[0.5, 1],
                   ecolor='magenta', capsize=10)
        pyplot.xticks([x + 0.6 / 2 for x in range(3)], [home, away],
                      rotation=360)
        plt.xlabel("Equipes")
        plt.ylabel("Buts Problables")
        plt.title("Combien du buts dans cette confrontation?")
        plt.show()
    elif fonction == "graph":
        resultgraph(home, away)
    elif fonction == "entrainement":
        traindata["FTR"].value_counts().plot.pie(explode=[0.025, 0.025, 0.025], shadow=True,
                                                 colors=['#ccff99', '#e65c00', '#6699ff'], autopct='%1.1f%%')
        plt.title("Visualisation des donnees d'entrainement")
        plt.show()
    elif fonction == "prediction":
        predictdata["FTR"].value_counts().plot.pie(explode=[0.025, 0.025, 0.025], shadow=True,
                                                   colors=['#ccff99', '#e65c00', '#6699ff'], autopct='%1.1f%%')
        plt.title("Visualisation des donnees de prediction")
        plt.show()
    elif fonction == "attaque":
        d = merged()
        h = d[home]["AttaqueHome"]
        a = d[away]["AttaqueAway"]
        print("************************************************")
        print("  " + home + " a pour force offensive {}".format(h))
        print("*************************************************")
        print("\n")
        print("************************************************")
        print("  " + away + " a pour force offensive {}".format(a))
        print("*************************************************")
        liste = [h, a]
        pyplot.bar(range(2), liste, width=0.6, color='red',
                   edgecolor='green', linewidth=2, yerr=[0.5, 1],
                   ecolor='magenta', capsize=10)
        pyplot.xticks([x + 0.6 / 2 for x in range(3)], [home, away],
                      rotation=360)
        plt.xlabel("Equipes")
        plt.ylabel("Force Offensive")
        plt.title("Comparaison des forces d'attaque")
        plt.show()
    elif fonction == "defense":
        d = merged()
        h = d[home]["DefenseHome"]
        a = d[away]["DefenseAway"]
        print("************************************************")
        print("  " + home + " a pour force défensive {}".format(h))
        print("*************************************************")
        print("\n")
        print("************************************************")
        print("  " + away + " a pour force défensive {}".format(a))
        print("*************************************************")
        liste = [h, a]
        pyplot.bar(range(2), liste, width=0.6, color='blue',
                   edgecolor='green', linewidth=2, yerr=[0.5, 1],
                   ecolor='magenta', capsize=10)
        pyplot.xticks([x + 0.6 / 2 for x in range(3)], [home, away],
                      rotation=360)
        plt.xlabel("Equipes")
        plt.ylabel("Force Defensive")
        plt.title("Comparaison des forces de defense")
        plt.show()
    elif fonction == "goals":
        d = merged()
        h = d[home]["ButsHome"]
        a = d[away]["ButsAway"]
        liste = [h, a]
        print(liste)
        pyplot.bar(range(2), liste, width=0.6, color='pink',
                   edgecolor='green', linewidth=2, yerr=[0.5, 1],
                   ecolor='magenta', capsize=10)
        pyplot.xticks([x + 0.6 / 2 for x in range(3)], ["Domicile", "Exterieur"],
                      rotation=360)
        plt.xlabel("Lieu du match")
        plt.ylabel("Nombre de buts")
        plt.title("Nombre de buts a domicile VS Nombre de buts a l'exterieur")
        plt.show()
    elif fonction == "precision":
        liste = [pprecision(), rprecision(), linearprecision(), logisticprecision()]
        pyplot.bar(range(4), liste, width=0.6, color='black',
                   edgecolor='green', linewidth=2, yerr=[0.5, 1, 2, 1],
                   ecolor='magenta', capsize=10)
        pyplot.xticks([x + 0.6 / 2 for x in range(5)], ['Poisson', 'Random', 'Linear', 'Logistic'],
                      rotation=360)
        plt.xlabel("Methodes")
        plt.ylabel("Precision")
        plt.title("Comparaison des methodes")
        plt.show()
    else:
        print("POISSON:")
        print("\n")
        chaine = pfulltimeresult(home, away)
        print("----------------------------------------------")
        print("| " + chaine)
        print("----------------------------------------------")
        print("\n")
        print("RANDOM FOREST:")
        print("\n")
        chaine = rfulltimeresult(home, away)
        print("----------------------------------------------")
        print("| " + chaine)
        print("----------------------------------------------")
        print("\n")
        print("LINEAR SVC:")
        print("\n")
        chaine = linearfulltimeresult(home, away)
        print("----------------------------------------------")
        print("| " + chaine)
        print("----------------------------------------------")
        print("\n")
        print("LOGISTIC REGRESSION:")
        print("\n")
        chaine = logisticfulltimeresult(home, away)
        print("----------------------------------------------")
        print("| " + chaine)
        print("----------------------------------------------")
        print("\n")


if __name__ == '__main__':
    main()

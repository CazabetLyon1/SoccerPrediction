Manuelle d’utilisation

Objectifs du projet :
Ce projet vise à réaliser des prédictions précisément sur des matchs de football. A Partir d’un tableau de données, il faut extraire les données que nous pourrons 
ensuite exploiter à cet effet.
Installation :
Pour compiler et tester ce projet, il est impératif d’avoir python (v2.7 minimum) installé sur la machine ainsi que plusieurs de ses modules (pandas, 
numpy, matplotlib, seaborn, entre autre…).
Ceci étant, pour l’exécution, il faut se placer dans le dossier ProjetInformatique et y ouvrir un terminal. Ce dossier contient le module Simulator.py, 
les fichiers .csv sur lesquelles on travaillera éventuellement, ainsi qu’un dossier contenant les utilitaires du projet.
Dans la ligne de commande, exécuter : 
    • python Simulator.py FILE HOME AWAY pour afficher les résultats de la rencontre entre HOME et AWAY d’après les différents algorithmes de précision.
    • python Simulator.py –f  nomFONCTION FILE HOME AWAY pour faire appel à une fonction particulière du programme.
Exemple : Pour un match Monaco VS Lyon on aura :
    • python Simulator.py Ligue1 Monaco Lyon pour afficher les résultats de la rencontre entre Monaco et Lyon d’après les différents algorithmes de précision.
    • python Simulator.py –f  butsprobables Ligue1 Monaco Lyon pour visualiser le nombre de buts probables que Lyon et Monaco pourraient marquer à l’issue de cette 
rencontre.
Liste des fonctions prises en compte :
    • butsprobables pour visualiser le nombre de buts susceptibles d’être marqués par les deux équipes en paramètre.
    • graph pour visualiser la matrice des différentes possibilités générée par la méthode poisson.
    • entrainement pour visualiser les données du fichier d’entraînement notamment les taux de victoires à domicile, à l’extérieur et de matchs nuls.
    • prediction pour visualiser les données du fichier de prédiction notamment les taux de victoires à domicile, à l’extérieur et de matchs nuls. 
    • attaque pour visualiser les forces d’attaque des deux équipes  en paramètre.
    • defense pour visualiser les forces de défense des deux équipes  en paramètre.
    • goals pour visualiser nombre total de buts marqués à domicile et ceux à l’extérieur.
    • précision pour visualiser les précisions des différentes méthodes implantées.
Remarque : L’option –f est facultative et n’est nécessaire que si l’on veut exécuter une fonction en particulier. La liste des options pourrait éventuellement être 
rallongée vue la quantité importante de données à visualiser. De plus HOME et AWAY doivent être dans la liste des équipes de FILE. Dans le cas contraire une exception 
est levée. Par exemple :                                          python Simulator.py Ligue1 Monaco Sevilla ne marcherait pas car Sevilla ne joue pas en Ligue1 mais en 
Liga. Enfin FILE doit être : Ligue1, Liga, SerieA ou League (France, Espagne, Italie ou Angleterre) car seuls ces quatre fichiers figurent dans le dossier du projet. 
Cependant, nous avons veillé à rendre notre code générique, ce qui fait qu’on peut facilement rajouter d’autres fichiers en cas de besoin. 
Organisation et explication du code:
    • Simulator.py constitue le cœur du projet. C’est là que les arguments de la ligne de commande sont interprétés.
    • FileRead.py du dossier Utils joue le  rôle le plus important dans la manipulation des données qui nous sont fournies.
    • Les autres fichiers du dossier Utils implémentent nos différentes méthodes de prédiction.
Résultats:
L’implémentation du projet que nous avons réalisée nous permet d’avoir une vue plutôt détaillée par rapport au fichier .csv que nous avions au départ.
Les résultats fournis par nos algorithmes de prédictions sont plus fiables les uns que les autres (on le sait grâce à la précision de chacun d’eux). En parlant de 
leurs précisions, nous avons été un peu déçus par leur performance. Cela pourrait éventuellement s’améliorer en prenant en compte plusieurs autres paramètres dans 
la prédiction.   

Lien vers le projet : 
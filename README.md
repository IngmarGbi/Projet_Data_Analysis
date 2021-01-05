# Projet_Data_Analysis
ESILV PROJET data Analysis


Classification d'image multispectrales selon la composition du sol
https://archive.ics.uci.edu/ml/datasets/Statlog+%28Landsat+Satellite%29

Le site indiquait de n'utiliser qu'un seul jeu de données et de le diviser en train/test, j'ai sélectionné le plus gros (environ 4000 éléments)

Le modèle final a une Accuracy de 89%.
Il est utilisable via le serveur Flask (Server_Flask_Soil_Gbiorczyk-Morel.py) utilisant le pickle (prediction_soil.pickle).
Le fichier (Request.py) est un exemple d'utilisation et d'appel au modèle prédictif.
Le format des Data envoyées est une liste des 36 descriptifs de pixel comme dans le fichier de données initial

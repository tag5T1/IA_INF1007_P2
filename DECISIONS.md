Choix du jeu de donnée
  Parties de League of Legends (LoL):
    format CSV,
    9880 lignes,
    cible quelle équipe gagnera selon les 10 premières minutes
    40 colonnes, catégorie équipe gagnante,
    License CC-0: Public domain,
    aucune données personelle: seulement l'ID de la partie qui référe des utilisateurs anonymes.
    => acceptable

  Viralité de chansons:
    format CSV,
    10000 lignes,
    cible si une chanson est virale selon ses paramètres
    17 colonnes, catégorie genre musical,
    License CC-0: Public domain,
    aucune données personelle: seulement l'ID de la chason et de l'artiste sans référence à de vrais noms.
    => acceptable

  Choix final: parties de LoL
    Paramètres des chasons trop subjectifs, comme "danceability" ou "energy". Paramètres des parties de LoL numériques et objectifs.
    Confirmé par chargeé de lab le 2026-10-23.

-------------------

Au chargement:
  Élimination des variables:
    * gameId: Elle ne représente aucune information
    * redFirstBlood: blueFirstBlood est déjà présente. Elles sont l'inverse l'une de l'autre.
    * redKills: redKills == blueDeaths
    * redDeaths: redDeaths == blueKills
    * redTotalExperience: redTotalExperience = blueTotalExperience - blueExperienceDiff
    * redTotalGold: redTotalGold = blueTotalGold - blueGoldDiff
    * redGoldDiff: redGoldDiff = -blueGoldDiff
    * redExperienceDiff: redExperienceDiff = -blueExperienceDiff
    * redGoldPerMin, blueGoldPerMin, blueCSPerMin, redCSPerMin: Pas besoin: on a le total et nos données sont des échantillons de 10 minutes exacgtement depuis le début de la partie.

Variable cible: "blueWins"
-> C'est la variable donnant la solution, de si les bleus ont gagné. Si oui, blueWins=1, Sinon blueWins=0

-------------------

train - test split: utilise un index fixe pour séparer le dataset en deux. Les données sont déjà aléatoires, donc inutile de mélanger.

Choix de métrique d'évaluation: exactitude.
Justification: la cible est binaire, donc un résultats sera toujours soit négatif, soit positif. Cela rend l'exactitude très efficace puisqu'il n'y a pas de proximité à la cible à prendre en compte: soit l'IA est complètement correct, soit elle ne l'est complètement pas.
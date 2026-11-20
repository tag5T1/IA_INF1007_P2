import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import json, os

def importer_donnees(source:str="./donnees/high_diamond_ranked_10min.csv") -> tuple[pd.DataFrame, pd.Series]:
    """Importe et retire certaines colonnes des données CSV."""
    donnees = pd.read_csv(source)

    columns = list(donnees.columns)
    columns.remove("gameId")
    columns.remove("redFirstBlood")
    columns.remove("redKills")
    columns.remove("redDeaths")
    columns.remove("redTotalExperience")
    columns.remove("redTotalGold")
    columns.remove("redGoldDiff")
    columns.remove("redExperienceDiff")
    columns.remove("redGoldPerMin")
    columns.remove("blueGoldPerMin")
    columns.remove("redCSPerMin")
    columns.remove("blueCSPerMin")
    donnees = donnees[columns]

    columns.remove("blueWins")
    X = donnees[columns]
    y = donnees["blueWins"]
    return (X, y)

def create_donnees_data() -> dict[str, int]:
    """Crée les données du modèle: Min, Max et Moyenne de chaque paramètre."""
    X, _ = importer_donnees()

    res = {}

    for x in X:
        res[x] = {"MIN": X[x].min().item(), "MAX": X[x].max().item(), "MOY": (X[x].sum()//len(X[x])).item()} # type: ignore

    return res

def split_data(donnees:tuple[pd.DataFrame,pd.Series]) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Sépare les données en données de test et données d'entrainement"""
    return tuple(train_test_split(donnees[0], donnees[1], test_size=0.2, random_state=1))

def get_historique() -> list[dict[str, str | dict[str, float]]]:
    """Charge l'historique des prédictions."""
    if os.path.exists(os.path.join(os.getcwd(), "historique.json")):
        with open(os.path.join(os.getcwd(), "historique.json"), encoding="utf-8", mode="r") as f:
            return json.load(f)
    return []

def set_historique(data:list[dict[str, str | dict[str, float]]]) -> None:
    """Sauvegarde l'historique des prédictions."""
    with open(os.path.join(os.getcwd(), "historique.json"), encoding="utf-8", mode="w") as f:
        json.dump(data, f, indent=2)

PARAMETRES_NOMS: dict[str, str] = {
    'blueWardsPlaced': "Wards bleu placés",
    'blueWardsDestroyed': "Wards bleu Détruits",
    'blueFirstBlood': "Bleu touché en premier",
    'blueKills': "Tués par bleu",
    'blueDeaths': "Bleu morts",
    'blueAssists': "Bleu assistés",
    'blueEliteMonsters': "Monstres bleu élite",
    'blueDragons': "Dragons bleu",
    'blueHeralds': "Heralds bleu",
    'blueTowersDestroyed': "Tours bleu détruites",
    'blueTotalGold': "Or total de bleu",
    'blueAvgLevel': "Niveau moyen des bleu",
    'blueTotalExperience': "Xp total des bleu",
    'blueTotalMinionsKilled': "Total de minions bleu tués",
    'blueTotalJungleMinionsKilled': "Total de jungle minions bleu tués",
    'blueGoldDiff': "Différence d'or des bleus",
    'blueExperienceDiff': "Différence d'Xp des bleus",
    'redWardsPlaced': "Wards rouge placés",
    'redWardsDestroyed': "Wards rouge détruits",
    'redAssists': "Rouge assité",
    'redEliteMonsters': "Monstres rouge élite",
    'redDragons': "Dragons rouge",
    'redHeralds': "Heralds rouge",
    'redTowersDestroyed': "Tours rouge détruite",
    'redAvgLevel': "Niveau moyen des rouge",
    'redTotalMinionsKilled': "Total de minions rouge tués",
    'redTotalJungleMinionsKilled': "Total de jungle minions rouge tués"
    }

PARAMETRES_TYPES: dict[str, str] = {
    'blueWardsPlaced': "STR",
    'blueWardsDestroyed': "STR",
    'blueFirstBlood': "BOOL",
    'blueKills': "STR",
    'blueDeaths': "STR",
    'blueAssists': "STR",
    'blueEliteMonsters': "STR",
    'blueDragons': "STR",
    'blueHeralds': "STR",
    'blueTowersDestroyed': "STR",
    'blueTotalGold': "STR",
    'blueAvgLevel': "STR",
    'blueTotalExperience': "STR",
    'blueTotalMinionsKilled': "STR",
    'blueTotalJungleMinionsKilled': "STR",
    'blueGoldDiff': "STR",
    'blueExperienceDiff': "STR",
    'redWardsPlaced': "STR",
    'redWardsDestroyed': "STR",
    'redAssists': "STR",
    'redEliteMonsters': "STR",
    'redDragons': "STR",
    'redHeralds': "STR",
    'redTowersDestroyed': "STR",
    'redAvgLevel': "STR",
    'redTotalMinionsKilled': "STR",
    'redTotalJungleMinionsKilled': "STR"
    }

if __name__ == "__main__":
    create_donnees_data()

    lol = importer_donnees()
    print(lol[0].columns)

    X_train, X_test, y_train, y_test = split_data(lol)

    print(X_train.head())
    print(X_test.head())

    graph = lol[0].plot()

    plt.savefig("Graphique_de_donnees.png")
    plt.show()
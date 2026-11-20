import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import json, os
from exceptions import DonneesInexistantesError, HistoriqueInvalideError

def importer_donnees(source:str="./donnees/high_diamond_ranked_10min.csv") -> tuple[pd.DataFrame, pd.Series]:
    """Importe et retire certaines colonnes des données CSV."""
    if os.path.exists(source):
        donnees = pd.read_csv(source)
    else:
        raise DonneesInexistantesError()

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

def get_historique(file_name:str="historique.json") -> list[dict[str, str | dict[str, float]]]:
    """Charge l'historique des prédictions."""
    if os.path.isfile(os.path.join(os.getcwd(), file_name)) and os.path.exists(os.path.join(os.getcwd(), file_name)):
        with open(os.path.join(os.getcwd(), file_name), encoding="utf-8", mode="r") as f:
            d = json.load(f)
            if type(d) is not list[dict[str, str | dict[str, float]]]:
                raise HistoriqueInvalideError()
            return json.load(f)
    return []

def set_historique(data:list[dict[str, str | dict[str, float]]]) -> None:
    """Sauvegarde l'historique des prédictions."""
    with open(os.path.join(os.getcwd(), "historique.json"), encoding="utf-8", mode="w") as f:
        json.dump(data, f, indent=2)

PARAMETRES_NOMS: dict[str, str] = {
    'blueWardsPlaced': "Wards placés - bleu",
    'blueWardsDestroyed': "Wards détruits - bleu",
    'blueFirstBlood': "Première élimination - bleu",
    'blueKills': "Éliminations - bleus",
    'blueDeaths': "Morts - bleus",
    'blueAssists': "Assistances - bleu",
    'blueEliteMonsters': "Monstres élite - bleu",
    'blueDragons': "Dragons - bleu",
    'blueHeralds': "Heralds - bleu",
    'blueTowersDestroyed': "Tours détruites - bleu",
    'blueTotalGold': "Or total - bleu",
    'blueAvgLevel': "Niveau moyen - bleu",
    'blueTotalExperience': "Xp total - bleu",
    'blueTotalMinionsKilled': "Total de minions tués - bleu",
    'blueTotalJungleMinionsKilled': "Total de jungle minions tués - bleu",
    'blueGoldDiff': "Différence d'or pour bleu",
    'blueExperienceDiff': "Différence d'xp pour bleu",
    'redWardsPlaced': "Wards placés - rouge",
    'redWardsDestroyed': "Wards détruits - rouge",
    'redAssists': "Assistances - rouge",
    'redEliteMonsters': "Monstres élites - rouge",
    'redDragons': "Dragons - rouge",
    'redHeralds': "Heralds - rouge",
    'redTowersDestroyed': "Tours détruites - rouge",
    'redAvgLevel': "Niveau moyen - rouge",
    'redTotalMinionsKilled': "Total de minions tués - rouge",
    'redTotalJungleMinionsKilled': "Total de jungle minions tués - rouge"
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
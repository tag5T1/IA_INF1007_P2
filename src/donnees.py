import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def importer_donnees(source:str="./donnees/high_diamond_ranked_10min.csv") -> tuple[pd.DataFrame,pd.Series]:
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

def create_donnees_data():
    X, _ = importer_donnees()

    res = {}

    for x in X:
        res[x] = {"MIN": X[x].min().item(), "MAX": X[x].max().item(), "MOY": (X[x].sum()//len(X[x])).item()} # type: ignore

    return res

def split_data(donnees:tuple[pd.DataFrame,pd.Series]) -> list:
    return train_test_split(donnees[0], donnees[1], test_size=0.2, random_state=1)

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

if __name__ == "__main__":
    create_donnees_data()



    lol = importer_donnees()
    print(lol[0].columns)

    X_train, X_test, y_train, y_test = split_data(lol)

    print(X_train.head())
    print(X_test.head())

    graph = lol[0].plot()

    plt.show()
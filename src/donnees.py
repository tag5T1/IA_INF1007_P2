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

def split_data(donnees:tuple[pd.DataFrame,pd.Series]) -> list:
    return train_test_split(donnees[0], donnees[1], test_size=0.2, random_state=1)

if __name__ == "__main__":
    lol = importer_donnees()
    print(lol[0].columns)

    X_train, X_test, y_train, y_test = split_data(lol)

    print(X_train.head())
    print(X_test.head())

    graph = lol[0].plot()

    plt.show()
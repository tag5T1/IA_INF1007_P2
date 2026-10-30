import pandas as pd
import matplotlib.pyplot as plt

def importer_donnees(source:str="./donnees/high_diamond_ranked_10min.csv") -> pd.DataFrame:
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
    return donnees

def train_test_split(donnees:pd.DataFrame, split_index:int) -> tuple[pd.DataFrame, pd.DataFrame]:
    if not (0 < split_index < donnees.shape[0] - 1):
        raise ValueError("Wrong split_index: Train or Test data would be empty!")
    return donnees[:split_index], donnees[split_index:]

if __name__ == "__main__":
    lol = importer_donnees()
    print(lol.columns)

    train, test = train_test_split(lol, 7500)

    print(train.head())
    print(test.head())

    graph = lol.plot()

    plt.show()
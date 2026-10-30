import pandas as pd
import matplotlib.pyplot as plt

def importer_donnees(source:str="./donnees/high_diamond_ranked_10min.csv") -> pd.DataFrame:
    donnees = pd.read_csv(source)

    columns = list(donnees.columns)
    columns.remove("gameId")
    columns.remove("redFirstBlood")
    donnees = donnees[columns]
    return donnees

def train_test_split(donnees:pd.DataFrame, split_index:int) -> tuple[pd.DataFrame, pd.DataFrame]:
    return donnees[:split_index], donnees[split_index:]

if __name__ == "__main__":
    lol = importer_donnees()
    print(lol.columns)

    train, test = train_test_split(lol, 7500)

    print(train.head())
    print(test.head())

    graph = lol.plot()

    plt.show()
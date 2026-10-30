import pandas as pd
import matplotlib.pyplot as plt

lol = pd.read_csv("./donnees/high_diamond_ranked_10min.csv")

columns = list(lol.columns)
columns.remove("gameId")
lol = lol[columns]

#print(columns)
#print(lol.head())

graph = lol.plot()

plt.show()
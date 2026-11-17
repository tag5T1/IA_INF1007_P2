import pandas as pd

def test_taille_valide():
    d = pd.read_csv("./donnees/high_diamond_ranked_10min.csv")
    assert 500 <= d.shape[0] <= 50000
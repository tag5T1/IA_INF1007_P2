import pandas as pd
import pytest
from exceptions import DonneesInexistantesError, HistoriqueInvalideError
from donnees import importer_donnees, get_historique

def test_taille_valide():
    d = pd.read_csv("./donnees/high_diamond_ranked_10min.csv")
    assert 500 <= d.shape[0] <= 50000

def test_importer_donnees():
    with pytest.raises(DonneesInexistantesError):
        importer_donnees(source="")

def test_get_historique_0():
    with pytest.raises(HistoriqueInvalideError):
        get_historique(file_name="EMPTY.json")

def test_get_historique_1():
    assert get_historique(file_name="") == []
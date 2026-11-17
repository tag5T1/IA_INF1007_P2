from donnees import importer_donnees

def test_taille_valide():
    assert 500 <= len(importer_donnees()[0]) <= 50000

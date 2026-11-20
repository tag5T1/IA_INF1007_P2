import sys
import numpy as np
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))
from modele import Modele
import pytest
from exceptions import InfosInvalideError, ModeleInexistantError

def test_acuracy():
    assert Modele().test_model() > 0.50

def test_compare_with_numpy():
    modele = Modele()
    assert modele.compare_with_numpy()

def test_load_model_0():
    with pytest.raises(InfosInvalideError):
        Modele.load_model(modele_data_name="EMPTY.json")

def test_load_model_1():
    with pytest.raises(ModeleInexistantError):
        Modele.load_model(modele_name="")
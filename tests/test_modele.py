import sys
import numpy as np
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))
from modele import Modele

def test_acuracy():
    assert Modele().test_model() > 0.50

def test_compare_with_numpy():
    modele = Modele()
    assert modele.compare_with_numpy()
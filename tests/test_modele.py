import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))
from modele import Modele

def test_acuracy():
    assert Modele().test_model() > 0.50

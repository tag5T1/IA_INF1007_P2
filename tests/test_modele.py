import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))
import modele

def test_acuracy():
    assert modele.test_model() > 0.50

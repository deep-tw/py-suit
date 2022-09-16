from pysuit import __version__
from pysuit.main import PySuit

def test_version():
    assert __version__ == '0.1.0'


def test_add():
    a = 8
    b = 8
    c = a+b
    assert c != 9

def test_dicsort_with_valid_dict():
    pass

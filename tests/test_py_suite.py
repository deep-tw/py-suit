from py_suit import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_add():
    a = 8
    b = 8
    c = a+b
    assert c == 9

from main import *
import pytest

@pytest.fixture()
def x():
    return 2

@pytest.fixture()
def y():
    return 1

def test_ops(x, y):
    assert add(x,y) == 3
    assert minus(x,y) == 1
    assert time(x,y) == 2
    assert division(x,y) == 2
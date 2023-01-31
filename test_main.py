from main import *
import pytest

@pytest.fixture(autouse=True)
def x():
    return 2

@pytest.fixture(autouse=True)
def y():
    return 1

def test_ops():
    assert add(x,y) == 3
    assert minus(x,y) == 1
    assert time(x,y) == 2
    assert division(x,y) == 2
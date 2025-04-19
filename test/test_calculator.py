from app import calculator
import pytest

def test_add():
    assert calculator.add(1, 2) == 3

def test_subtract():
    assert calculator.subtract(5, 2) == 3

def test_multiply():
    assert calculator.multiply(3, 4) == 12

def test_divide():
    assert calculator.divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

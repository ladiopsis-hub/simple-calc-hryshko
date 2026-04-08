# tests/test_calculator.py

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5.0

def test_subtract():
    assert subtract(10, 4) == 6.0

def test_multiply():
    assert multiply(3, 4) == 12.0

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
# calculator.py — refactored with validation

from validator import validate_inputs

def add(a, b):
    if not validate_inputs(a, b):
        raise TypeError("Invalid input")
    return float(a) + float(b)

def subtract(a, b):
    if not validate_inputs(a, b):
        raise TypeError("Invalid input")
    return float(a) - float(b)

def multiply(a, b):
    if not validate_inputs(a, b):
        raise TypeError("Invalid input")
    return float(a) * float(b)

def divide(a, b):
    if not validate_inputs(a, b):
        raise TypeError("Invalid input")
    if float(b) == 0:
        raise ValueError("Cannot divide by zero")
    return float(a) / float(b)

# production version: 1.1
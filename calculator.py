# calculator.py — with logging added

import logging
from validator import validate_inputs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add(a, b):
    if not validate_inputs(a, b):
        raise TypeError("Invalid input")
    result = float(a) + float(b)
    logger.info(f"add({a}, {b}) = {result}")
    return result

def subtract(a, b):
    if not validate_inputs(a, b):
        raise TypeError("Invalid input")
    result = float(a) - float(b)
    logger.info(f"subtract({a}, {b}) = {result}")
    return result

def multiply(a, b):
    if not validate_inputs(a, b):
        raise TypeError("Invalid input")
    result = float(a) * float(b)
    logger.info(f"multiply({a}, {b}) = {result}")
    return result

def divide(a, b):
    if not validate_inputs(a, b):
        raise TypeError("Invalid input")
    if float(b) == 0:
        raise ValueError("Cannot divide by zero")
    result = float(a) / float(b)
    logger.info(f"divide({a}, {b}) = {result}")
    return result

# production version: 1.1

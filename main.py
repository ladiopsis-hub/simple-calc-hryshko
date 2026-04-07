# main.py — entry point

from calculator import add, subtract, multiply, divide
from formatter import format_result, format_error

operations = [
    ("+", 10, 5),
    ("-", 10, 5),
    ("*", 10, 5),
    ("/", 10, 5),
    ("/", 10, 0),
]

for op, a, b in operations:
    try:
        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        elif op == "/":
            result = divide(a, b)
        print(format_result(op, a, b, result))
    except ValueError as e:
        print(format_error(str(e)))
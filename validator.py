# validator.py — input validation

def is_valid_number(value):
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False

def validate_inputs(a, b):
    return is_valid_number(a) and is_valid_number(b)
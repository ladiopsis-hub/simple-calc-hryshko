# formatter.py — result formatting

def format_result(operation, a, b, result):
    return f"{a} {operation} {b} = {result}"

def format_error(message):
    return f"Error: {message}"
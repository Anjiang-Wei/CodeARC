def calculate_expression(num1: float, operation: str, num2: float) -> float:
    try:
        if operation in ['+', '-', '*', '/']:
            return eval(f"{num1} {operation} {num2}")
        else:
            return None
    except (ZeroDivisionError, SyntaxError):
        return None


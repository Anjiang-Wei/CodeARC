def calculate(operator: str, value1: float, value2: float) -> float:
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '/':
        return value1 / value2
    if operator == '*':
        return value1 * value2


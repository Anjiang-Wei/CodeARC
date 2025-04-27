def calculate(x: float, y: float, op: str) -> float | str:
    if isinstance(x, (int, float)) and isinstance(y, (int, float)) and op in '+-*/':
        # Perform the operation based on the operator
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
    else:
        # Return 'unknown value' if inputs are invalid
        return 'unknown value'


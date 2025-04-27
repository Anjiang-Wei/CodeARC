def perform_operation(a: float, b: float, operator: str) -> float:
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]


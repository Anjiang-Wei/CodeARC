def calculate_operation(a: float, b: float, res: float) -> str:
    return {
        a + b: "addition",
        a - b: "subtraction",
        a * b: "multiplication",
        a / b: "division"
    }.get(res, "invalid result")


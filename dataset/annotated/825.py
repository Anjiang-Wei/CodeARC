def perform_operation(a: float, o: str, b: float) -> float | None:
    from operator import add, sub, mul, truediv
    D = {'+': add, '-': sub, '*': mul, '/': truediv}
    
    try:
        return D[o](a, b)
    except:
        return None  # Return None if operation is not valid or division by zero occurs


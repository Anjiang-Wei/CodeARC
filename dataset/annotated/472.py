def fibonacci_divisor_sequence(divisor: int, iterations: int) -> tuple[int, int]:
    a = divisor
    b = divisor if iterations != 0 else 0
    
    for _ in range(iterations):
        c = b
        b = a
        a = b + c
    
    return a, b


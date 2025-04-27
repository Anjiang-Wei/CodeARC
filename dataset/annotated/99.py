def find_linear_combination_solution(a: int, b: int, n: int) -> tuple[int, int] | None:
    i = 0
    while i * a <= n:
        if (n - (i * a)) % b == 0: 
            return (i, (n - (i * a)) // b)
        i = i + 1
    return None


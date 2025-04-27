def sum_of_powers(m: int, n: int) -> int:
    return sum(i**j for i in range(m+1) for j in range(n+1))


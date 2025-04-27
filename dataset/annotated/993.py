def sum_of_multiples_in_range(n: int, m: int) -> int | str:
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'


def is_number_sorted(n: int) -> bool:
    s = list(str(n))
    return s == sorted(s)


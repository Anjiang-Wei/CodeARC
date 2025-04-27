def can_maintain_balance(
    f0: int, p: float, c0: int, n: int, i: float
) -> bool:
    for _ in range(n-1):
        f0 = int(f0 * (100 + p) / 100 - c0)
        c0 = int(c0 * (100 + i) / 100)
        if f0 < 0:
            return False
    return True


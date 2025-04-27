def is_remainder_multiple(a: int, b: int, n: int) -> bool:
    remainder = int((a / b + 0.05) * 10) % 10
    return remainder > 0 and remainder % n == 0


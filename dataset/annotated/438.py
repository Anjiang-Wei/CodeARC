def dig_pow(n: int, p: int) -> int:
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    # Check if s is divisible by n
    return s // n if s % n == 0 else -1


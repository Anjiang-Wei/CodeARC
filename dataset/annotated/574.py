def find_safe_position(n: int, k: int) -> int:
    v = 0
    for i in range(1, n + 1):
        v = (v + k) % i
    return v + 1


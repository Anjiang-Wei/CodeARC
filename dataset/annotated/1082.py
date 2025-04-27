def distribute_items_equally(m: int, n: int) -> list[int]:
    if n <= 0:
        return []
    q, r = divmod(max(m, 0), n)
    return [q + (i < r) for i in range(n)]


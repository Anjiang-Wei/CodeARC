def sum_excluding_extremes(arr: list[int]) -> int:
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


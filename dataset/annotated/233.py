def find_min_elements_to_reach_sum(arr: list[int], k: int) -> int:
    arr = sorted(arr)
    s = 0
    for i, v in enumerate(arr):
        s += v
        if s >= k:
            return i


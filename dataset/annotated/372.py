def sum_adjacent_until_single(arr: list[int]) -> int:
    while len(arr) > 1:
        arr = [x + y for x, y in zip(arr, arr[1:])]
    return arr[0]


def find_first_odd_index(arr: list[int]) -> int:
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            return i
    return -1


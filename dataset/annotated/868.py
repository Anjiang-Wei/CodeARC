def count_pairs_with_difference(arr: list[int], n: int) -> int:
    num = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == n:
                num += 1
    return num


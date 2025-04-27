def count_pairs_with_sum(arr: list[int], target_sum: int) -> float:
    cnt = 0
    for n in arr:
        cnt += arr.count(target_sum - n)
        if target_sum - n == n:
            cnt -= 1
    return cnt / 2


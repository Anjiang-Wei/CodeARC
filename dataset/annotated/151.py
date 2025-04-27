def count_unique_pairs(arr: list, n: int) -> int: 
    cnt = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] != arr[j]): 
                cnt += 1
    return cnt


def is_symmetric_pairs(arr: list[int]) -> bool:
    from collections import Counter
    
    c = Counter(arr)
    # Check if array is not empty and for each element k, count of k is equal to count of -k
    return bool(arr) and all(c[k] == c[-k] for k in c)


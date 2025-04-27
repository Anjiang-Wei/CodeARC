def max_subsequence_product(arr: list[int]) -> int:   
    # record the correspond ending element to maintain the increasing subsequence
    ret = max_ending = min_ending = (arr[0], arr[0])
    for n in arr[1:]:
        if n > max_ending[1]:
            max_ending = max((max_ending[0] * n, n), max_ending, key=lambda x: x[0])
        else:
            max_ending = (n, n)
        if n > min_ending[1]:
            min_ending = min((min_ending[0] * n, n), min_ending, key=lambda x: x[0])
        else:
            min_ending = (n, n)
        ret = max(ret, max_ending, min_ending, key=lambda x: x[0])
    return ret[0]


def filter_consecutive_sums(x: list, t: int) -> list:
    arr = [x[0]]
    for c in x[1:]:
        if c + arr[-1] != t:
            arr.append(c)
    return arr


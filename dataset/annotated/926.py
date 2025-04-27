def is_enclosed_by_zeros(x: list[int]) -> bool:
    while x and x[0] != 0 and x[-1] != 0:
        x = x[1:-1]
    # Check if there are more than 2 zeros and all elements are zero
    return len(x) > 2 and set(x) == {0}


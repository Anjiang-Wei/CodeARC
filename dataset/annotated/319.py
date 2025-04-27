def kangaroos_meet(start1: int, jump1: int, start2: int, jump2: int) -> bool:
    if jump1 == jump2:
        return start1 == start2
    cross, remainder = divmod(start1 - start2, jump2 - jump1)
    # Check if they meet at a non-negative step and remainder is zero
    return cross >= 0 and remainder == 0


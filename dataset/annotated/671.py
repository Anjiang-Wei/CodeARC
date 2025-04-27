def find_min_remainder(a: int, x: int) -> int:
    # Calculate the remainder of a divided by x
    remainder = a % x
    # Calculate the negative remainder of a divided by x
    negative_remainder = -a % x
    # Return the minimum of the two remainders
    return min(remainder, negative_remainder)


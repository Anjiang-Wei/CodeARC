def is_divisible_by_3(s: str) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    # Convert the string to an integer and check divisibility by 3
    return int(s) % 3 == 0


def add_digits_of_number(num: int) -> int:
    """
    :type num: int
    :rtype: int
    """
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


def find_nth_digit(n: int) -> int:
    """
    :param n: The position of the digit in the sequence.
    :return: The nth digit in the sequence.
    """
    i = count = 9
    while count < n:
        i *= 10
        count += i * len(str(i))

    div, mod = divmod(n - (count - i * len(str(i))), len(str(i)))
    target = (i // 9 - 1) + div

    if mod == 0:
        return int(str(target)[-1])
    else:
        return int(str(target + 1)[mod - 1])


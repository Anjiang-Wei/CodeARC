def round_away_from_zero(value: str) -> int:
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> round_away_from_zero("10")
    10
    >>> round_away_from_zero("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example round_away_from_zero("14.5") should
    return 15 and round_away_from_zero("-14.5") should return -15.
    '''

    val = float(value)
    if abs(val - int(val)) != 0.5:
        return round(val)
    if val > 0:
        return int(val) + 1
    else:
        return int(val) - 1


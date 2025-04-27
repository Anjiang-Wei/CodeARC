def is_balanced_brackets(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> is_balanced_brackets("(")
    False
    >>> is_balanced_brackets("()")
    True
    >>> is_balanced_brackets("(()())")
    True
    >>> is_balanced_brackets(")(()")
    False
    """

    cnt = 0
    for x in brackets:
        if x == "(": cnt += 1
        if x == ")": cnt -= 1
        if cnt < 0: return False
    return cnt == 0


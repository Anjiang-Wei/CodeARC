def is_bracket_balanced(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> is_bracket_balanced("<")
    False
    >>> is_bracket_balanced("<>")
    True
    >>> is_bracket_balanced("<<><>>")
    True
    >>> is_bracket_balanced("><<>")
    False
    """
    cnt = 0
    for x in brackets:
        if x == "<": cnt += 1
        if x == ">": cnt -= 1
        if cnt < 0: return False
    return cnt == 0


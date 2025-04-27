def solution(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> solution("<")
    False
    >>> solution("<>")
    True
    >>> solution("<<><>>")
    True
    >>> solution("><<>")
    False
    """
    cnt = 0
    for x in brackets:
        if x == "<": cnt += 1
        if x == ">": cnt -= 1
        if cnt < 0: return False
    return cnt == 0


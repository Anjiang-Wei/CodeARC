def solution(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> solution('Hello')
    'hELLO'
    """
    return "".join(map(lambda x: x.swapcase(), string))


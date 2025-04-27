def toggle_character_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> toggle_character_case('Hello')
    'hELLO'
    """
    return "".join(map(lambda x: x.swapcase(), string))


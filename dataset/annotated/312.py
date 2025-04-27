def can_be_constructed_from_repeated_subpattern(string: str) -> bool:
    # Check if the string can be constructed by repeating a subpattern
    return (string * 2).find(string, 1) != len(string)


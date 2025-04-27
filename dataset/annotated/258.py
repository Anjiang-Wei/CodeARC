def contains_abc_in_shortened_string(s: str) -> bool:
    while len(s) > 4:
        s = s[1:-1]
    return 'abc' in s


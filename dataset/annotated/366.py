def merge_and_filter_strings(s1: str, s2: str) -> str:
    s = [''] * (len(s1) + len(s2))
    s[::2], s[1::2] = s1, s2
    # Filter out digits and join the characters
    return ''.join(c for c in s if not c.isdigit()).strip()


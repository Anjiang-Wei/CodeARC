def repeat_and_capitalize_sorted_chars(s: str) -> str:
    return ",".join((c * (ord(c) - 96)).capitalize() for c in sorted(s.lower()))


def retain_case_symmetric_characters(s: str) -> str:
    seen = set(s)
    return ''.join(a for a in s if a.swapcase() in seen)


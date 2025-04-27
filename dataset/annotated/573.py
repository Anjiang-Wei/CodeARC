def swap_ab_characters(s: str) -> str:
    return s.translate(str.maketrans('ab', 'ba'))


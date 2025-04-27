def replace_vowels_with_exclamation(s: str) -> str:
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


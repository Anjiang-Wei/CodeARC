def rearrange_vowels_and_consonants(s: str) -> str:
    # Separate vowels and non-vowels, then concatenate them
    return ''.join(sorted(s, key=lambda k: k in 'aeiou'))


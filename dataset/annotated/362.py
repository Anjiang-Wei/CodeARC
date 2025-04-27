def longest_vowel_sequence(s: str) -> int:
    return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))


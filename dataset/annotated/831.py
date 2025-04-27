def calculate_vowel_contribution(input: str) -> int:
    vowels = set('aeiouAEIOU')
    s = t = 0
    for c, e in enumerate(input, 1):
        if e in vowels:
            t += c
        s += t
    return s


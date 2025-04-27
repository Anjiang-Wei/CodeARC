def find_missing_vowel(x: str) -> int:
    return ['aeiou'.index(i) for i in 'aeiou' if i not in x][0]


def construct_missing_letters(s: str) -> str:
    from collections import Counter
    from string import ascii_lowercase
    
    c = Counter(s)
    m = max(c.values())
    
    # Construct the result by repeating each missing letter the required number of times
    return ''.join(letter * (m - c[letter]) for letter in ascii_lowercase)


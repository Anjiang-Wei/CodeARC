def has_no_consecutive_vowels_or_consonants(s: str) -> bool:
    import re
    # Check for consecutive vowels or consonants
    return not re.search('[aeiou]{2}|[^aeiou]{2}', s)


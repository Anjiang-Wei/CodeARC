def remove_internal_vowels(s: str) -> str:
    from re import sub, I
    # Use regex to remove vowels except if they are the first or last character
    return sub(r"(?<!^)[aeiou](?=.)", '', s, flags=I)


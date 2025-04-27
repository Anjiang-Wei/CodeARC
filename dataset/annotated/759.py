def replace_with_umlauts(s: str) -> str:
    UMLAUTS = {
        'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü', 'Y': 'Ÿ',
        'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü', 'y': 'ÿ'
    }
    # Replace each character in the string with its umlaut version if available
    return ''.join(UMLAUTS.get(a, a) for a in s)


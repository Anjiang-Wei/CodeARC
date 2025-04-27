def replace_vowels_with_positions(string: str) -> str:
    vowels = 'aeiouAEIOU'
    # Replace vowels with their respective positions
    return ''.join(x if x not in vowels else str(n + 1) for n, x in enumerate(string))


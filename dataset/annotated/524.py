def shift_characters(p: str) -> str:
    return ''.join(
        chr((ord(j) + i % 3 + (i - 1) // 3 - 97) % 26 + 97) if j != ' ' and i != 0 else j 
        for i, j in enumerate(p)
    )


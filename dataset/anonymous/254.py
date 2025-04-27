def solution(name):
    import re

    REPLACMENTS = ["BFPV", "CGJKQSXZ", "DT", "L", "MN", "R"]
    ER1, ER2 = "HW", "AEIOUY"

    TABLE_ERASE1 = str.maketrans("", "", ER1)
    TABLE_NUMS = str.maketrans(''.join(REPLACMENTS), ''.join(str(n) * len(elt) for n, elt in enumerate(REPLACMENTS, 1)))
    TABLE_ERASE2 = str.maketrans("", "", ER2)

    def formatSoundex(w):
        # Preserve the first letter if it's in ER1 or ER2
        s = w[0] * (w[0] in ER1 + ER2) + re.sub(r'(\d)\1*', r'\1', w.translate(TABLE_ERASE1).translate(TABLE_NUMS)).translate(TABLE_ERASE2)
        # Ensure the first character is a letter and append zeros if necessary
        return ((w[0] if s[0].isdigit() else s[0]) + s[1:] + "000")[:4]

    # Process each word in the input name
    return ' '.join(formatSoundex(w.upper()) for w in name.split(" "))


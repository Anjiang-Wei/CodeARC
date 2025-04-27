def vigenere_transform(text: str, key: str, mode: str = 'encode') -> str:
    from string import ascii_lowercase as aLow
    import re

    def rotateWord(w, alpha, dct, d):
        lst = []
        for i, c in enumerate(w.lower(), 1):
            transChar = alpha[(dct[c] + i * d) % 26]
            if w[i - 1].isupper():
                transChar = transChar.upper()
            lst.append(transChar)
        return ''.join(lst)

    def process(text, key, d):
        remains, alpha = set(aLow), []
        for c in key + aLow:
            if c in remains:
                remains.remove(c)
                alpha.append(c)
        alpha = ''.join(alpha)
        dct = {c: i for i, c in enumerate(alpha)}
        return re.sub(r'[a-zA-Z]+', lambda m: rotateWord(m.group(), alpha, dct, d), text)

    if mode == 'encode':
        return process(text, key, 1)
    elif mode == 'decode':
        return process(text, key, -1)
    else:
        raise ValueError("Mode should be 'encode' or 'decode'")


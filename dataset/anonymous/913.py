def solution(text, n, mode='encrypt'):
    if text in ("", None) or n <= 0:
        return text

    if mode == 'encrypt':
        for _ in range(n):
            text = text[1::2] + text[::2]
        return text
    elif mode == 'decrypt':
        ndx = len(text) // 2
        for _ in range(n):
            a = text[:ndx]
            b = text[ndx:]
            text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
        return text
    else:
        raise ValueError("Mode should be either 'encrypt' or 'decrypt'")


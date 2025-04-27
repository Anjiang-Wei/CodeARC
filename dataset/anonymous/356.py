def solution(s, mode='encode'):
    """
    :type s: str
    :type mode: str
    :rtype: str
    """
    if mode == 'encode':
        t = str.maketrans("aeiou", "12345")
        return s.translate(t)
    elif mode == 'decode':
        t = str.maketrans("12345", "aeiou")
        return s.translate(t)
    else:
        raise ValueError("Invalid mode. Use 'encode' or 'decode'.")


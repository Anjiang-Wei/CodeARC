def solution(s):
    # Convert the hexadecimal string to an RGB dictionary
    return {i: int(s[j:j+2], 16) for i, j in zip('rgb', [1, 3, 5])}


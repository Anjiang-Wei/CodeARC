def solution(key, message):
    result = []
    key %= 26  # Normalize the key

    for char in message:
        if 'a' <= char <= 'z':  # Shift lowercase letters
            new_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':  # Shift uppercase letters
            new_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            new_char = char  # Keep non-alphabet characters unchanged

        result.append(new_char)

    return ''.join(result)


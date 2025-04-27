def solution(message, code):
    return ''.join(message[-1-i] for i, c in enumerate(bin(code)[::-1]) if c == '1' and i < len(message))[::-1]


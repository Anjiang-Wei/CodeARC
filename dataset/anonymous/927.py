def solution(a, b):
    return "".join(f"{int(x, 16) ^ int(y, 16):x}" for x, y in zip(a, b))


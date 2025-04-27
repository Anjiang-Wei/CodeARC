def solution(text, rule):
    return "".join(chr((ord(i) + rule) % 256) for i in text)


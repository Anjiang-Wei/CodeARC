def solution(str1):
    return sum(ord(ch.lower()) - ord('a') == i for i, ch in enumerate(str1))


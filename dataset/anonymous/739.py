def solution(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return -1
    elif len(s) == 1:
        return 0

    result = len(s)
    for ch in range(ord('a'), ord('z') + 1):
        if s.find(chr(ch)) == -1:
            continue
        if s.find(chr(ch)) == s.rfind(chr(ch)):
            result = min(result, s.find(chr(ch)))
    return result if result < len(s) else -1


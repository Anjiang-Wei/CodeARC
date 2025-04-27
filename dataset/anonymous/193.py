import re

def solution(text, pattern):
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        return (text[s:e], s, e)
    return None


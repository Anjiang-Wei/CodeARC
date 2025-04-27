import re

def solution(s):
    return re.sub(r'(.)\1+', lambda m: m.group().swapcase(), s)


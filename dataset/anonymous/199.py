import re

def solution(text):
    patterns = 'ab{3}?'
    return re.search(patterns, text)


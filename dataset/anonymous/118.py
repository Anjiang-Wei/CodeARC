import re

def solution(text):
    patterns = 'ab{2,3}'
    return re.search(patterns, text) is not None


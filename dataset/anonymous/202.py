import re

def solution(text):
    patterns = 'a.*?b$'
    return re.search(patterns, text)


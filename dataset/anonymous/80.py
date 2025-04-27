import re

def solution(text):
    return bool(re.match('^[a-z]+(_[a-z]+)*$', text))


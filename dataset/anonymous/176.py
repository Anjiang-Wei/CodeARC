import re

def solution(text):
    return re.search(r'\Bz\B', text) is not None


import re

def solution(text):
    return re.sub("[ ,.]", ":", text)


import re

def solution(string): 
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
    return re.search(regex, string)


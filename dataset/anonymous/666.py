def solution(s):
    # Remove all exclamation marks and append them to the end
    return s.replace('!', '') + s.count('!') * '!'


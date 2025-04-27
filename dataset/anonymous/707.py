def solution(s):
    import re
    # Split the string by non-word characters and underscores, capitalize each word, and join them
    return "".join([w.capitalize() for w in re.split(r"\W|_", s)])


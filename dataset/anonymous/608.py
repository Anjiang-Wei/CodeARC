def solution(s):
    import re
    # Check for consecutive vowels or consonants
    return not re.search('[aeiou]{2}|[^aeiou]{2}', s)


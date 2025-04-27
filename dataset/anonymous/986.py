def solution(p, r):
    import re
    # Create a regex pattern that matches any suffix of the slogan `p`
    reg = re.compile("|".join([re.escape(p[i:]) for i in range(len(p))]))
    # Find all matches of the pattern in the string `r` and return the count
    return len(re.findall(reg, r))


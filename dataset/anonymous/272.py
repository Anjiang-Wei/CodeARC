def solution(x, s):
    import re
    # Find all mating pairs using regex
    pairs = re.findall(r"B8|8B", s)
    # Join pairs into a single string and check if the count is sufficient
    return ["".join(pairs), len(pairs) >= x]


def solution(s):
    import re
    # Find all sequences of digits in the string and convert them to integers, then sum them up
    return sum(int(x) for x in re.findall(r"(\d+)", s))


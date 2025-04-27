def solution(s):
    import re
    # Find all number groupings in the string and convert them to integers
    numbers = map(int, re.findall(r"(\d+)", s))
    # Return the maximum number found
    return max(numbers)


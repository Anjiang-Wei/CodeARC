def solution(s):
    from itertools import groupby
    # Calculate the number of characters to remove by subtracting the length of grouped characters from the original length
    return len(s) - len(list(groupby(s)))


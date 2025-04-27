def solution(column, day, night):
    from math import ceil
    # Calculate the number of days required for the snail to reach the top
    return max(ceil((column - night) / (day - night)), 1)


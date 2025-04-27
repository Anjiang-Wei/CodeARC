def solution(s):
    if not s or len(s) == 1:
        return -1
    # Calculate the total candies needed to make all equal to the max
    return len(s) * max(s) - sum(s)


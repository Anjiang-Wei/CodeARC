def solution(arr):
    odds = [x for x in arr if x % 2 != 0]
    evens = [x for x in arr if x % 2 == 0]
    # Return the outlier based on which list is shorter
    return odds[0] if len(odds) < len(evens) else evens[0]


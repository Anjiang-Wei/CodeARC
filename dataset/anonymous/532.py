def solution(numbers):
    lst = sorted(numbers)
    # Calculate the maximum difference between successive elements
    return max(b - a for a, b in zip(lst, lst[1:]))


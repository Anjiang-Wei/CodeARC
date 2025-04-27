def solution(array):
    # Calculate the maximum product of adjacent elements
    return max(a * b for a, b in zip(array, array[1:]))


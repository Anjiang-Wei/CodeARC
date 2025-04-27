def solution(arr):
    # Calculate the greatest distance between matching numbers in the array
    return max(i - arr.index(x) for i, x in enumerate(arr))


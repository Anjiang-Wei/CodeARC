def solution(arr):
    s = set(arr)
    # Check if the array is not empty and every element has a neighbor n-1 or n+1
    return bool(arr) and all(n + 1 in s or n - 1 in s for n in s)


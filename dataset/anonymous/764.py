def solution(arr, n):
    # Calculate the effective rotation
    n = n % len(arr)
    # Rotate the array by slicing
    return arr[-n:] + arr[:-n]


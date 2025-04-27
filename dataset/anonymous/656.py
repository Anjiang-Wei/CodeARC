def solution(arr):
    m = arr.index(min(arr))
    # Check if the array is equal to its sorted version when rotated
    return sorted(arr) == (arr[m:] + arr[:m])


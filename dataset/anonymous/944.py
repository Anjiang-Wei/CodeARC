def solution(arr, n):
    i = 0
    while i < len(arr):
        x = arr[i]
        # Adjust the current position value based on comparison with n
        arr[i] += 1 if x < n else -1
        # Move to the next position based on the current value
        i += x
    # Count how many elements are equal to n
    return arr.count(n)


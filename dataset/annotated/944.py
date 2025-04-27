def count_elements_equal_to_n(arr: list[int], n: int) -> int:
    i = 0
    while i < len(arr):
        x = arr[i]
        # Adjust the current position value based on comparison with n
        arr[i] += 1 if x < n else -1
        # Move to the next position based on the current value
        i += x
    # Count how many elements are equal to n
    return arr.count(n)


def find_smallest_non_divisor(arr: list[int]) -> int:
    n = 2
    while True:
        # Check if n is not a divisor of any element in arr
        if all(x % n != 0 for x in arr):
            return n
        n += 1


def find_greatest_common_divisor(arr: list[int]) -> int:
    for n in range(max(arr) - 1, 0, -1):
        # Check if all elements have the same remainder when divided by n
        if len({x % n for x in arr}) == 1:
            return n
    return -1


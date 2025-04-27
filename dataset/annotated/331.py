def is_sum_divisible_and_positive(arr: list[int]) -> bool:
    return sum(arr) % len(arr) == 0 and sum(arr) > 0


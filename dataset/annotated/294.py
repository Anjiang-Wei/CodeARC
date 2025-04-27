def find_number_properties(arr: list[int]) -> list[int]:
    from collections import Counter

    n = 1
    factor_count = Counter(arr)
    for factor in arr:
        n *= factor

    divisor_count = 1
    for count in factor_count.values():
        divisor_count *= (count + 1)

    smallest_divisor = min(arr)
    largest_divisor = n // smallest_divisor

    return [n, divisor_count - 1, smallest_divisor, largest_divisor]


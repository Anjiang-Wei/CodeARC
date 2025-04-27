def filter_odd_numbers(numbers: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 1, numbers))


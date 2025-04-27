def count_numbers_without_five(start: int, end: int) -> int:
    return sum('5' not in str(i) for i in range(start, end + 1))


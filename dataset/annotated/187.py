def find_second_smallest(numbers: list[int]) -> int | None:
    sorted_set = sorted(set(numbers))
    if len(sorted_set) < 2:
        return None
    return sorted_set[1]


def find_first_non_consecutive(arr: list[int]) -> int | None:
    if not arr:
        return None  # Return None for empty array
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]  # Return the first non-consecutive number
    return None  # Return None if all elements are consecutive


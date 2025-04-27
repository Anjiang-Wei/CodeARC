def filter_divisible_elements(lst: list[int]) -> list[int]:
    return [lst[i] for i in range(1, len(lst)) if lst[i] % i == 0]


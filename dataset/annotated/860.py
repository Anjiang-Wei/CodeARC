def count_memory_reallocation_cycles(banks: list[int]) -> int:
    seen = set()
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        number = max(banks)
        index = banks.index(number)
        banks[index] = 0
        while number:
            index = (index + 1) % len(banks)  # Use len(banks) for flexibility
            banks[index] += 1
            number -= 1
    return len(seen)


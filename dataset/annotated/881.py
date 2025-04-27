def find_unique_parity_index(numbers: str) -> int:
    e = [int(i) % 2 == 0 for i in numbers.split()]
    # Check if there is only one even number or one odd number
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


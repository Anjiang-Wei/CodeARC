def count_unique_digits(seq: list[str]) -> int:
    # Convert the sequence to a single string and find unique digits
    return len(set(''.join(seq)))


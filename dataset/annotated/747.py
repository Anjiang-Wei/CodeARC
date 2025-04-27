def has_duplicates(*args: int) -> bool:
    return len(args) != len(set(args))


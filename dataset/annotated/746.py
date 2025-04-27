def is_subsequence_ignoring_case(main_string: str, subsequence: str) -> bool:
    it = iter(main_string.lower())
    # Check if all characters in 'subsequence' are in 'main_string' in order
    return all(c in it for c in subsequence.lower())


def are_all_chars_in_first_string(arr: list[str]) -> bool:
    return set(arr[1].lower()) <= set(arr[0].lower())


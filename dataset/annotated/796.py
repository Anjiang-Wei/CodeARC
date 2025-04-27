def categorize_list_length(lst: list) -> str:
    return ["empty", "singleton", "longer"][min(len(lst), 2)]


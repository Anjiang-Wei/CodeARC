def process_name(name: str) -> list[str]:
    # If the name length is greater than 2, return both full and truncated names
    # Otherwise, return the name as is
    return [name, name[:2]] if len(name) > 2 else [name]


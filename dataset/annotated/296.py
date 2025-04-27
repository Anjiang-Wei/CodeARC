def remove_isolated_bug(s: str) -> str:
    import re
    # Use regex to remove 'bug' not followed by 's'
    return re.sub(r'bug(?!s)', '', s)


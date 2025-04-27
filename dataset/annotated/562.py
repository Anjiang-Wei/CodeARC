def rotate_string(string: str, step: int) -> str:
    i = (step % len(string)) if string else 0
    return f"{string[-i:]}{string[:-i]}"

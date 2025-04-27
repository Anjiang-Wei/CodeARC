def find_first_repeated_character(s: str) -> str | None:
    for index, c in enumerate(s):
        if s[:index + 1].count(c) > 1:
            return c
    return None


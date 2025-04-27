def move_exclamation_marks_to_end(s: str) -> str:
    return s.replace('!', '') + '!' * (len(s) - len(s.rstrip('!')))


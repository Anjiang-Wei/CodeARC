def is_wall_intact(new: str, old: str) -> bool:
    return all(patch == ' ' for patch, tile in zip(new, old) if tile in '\\/')


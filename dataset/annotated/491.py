def does_name_play_banjo(name: str) -> str:
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"


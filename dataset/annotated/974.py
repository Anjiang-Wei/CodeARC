def calculate_coffee_effect(events: list[str]) -> str | int:
    cs = {'cw': 1, 'CW': 2, 'cat': 1, 'CAT': 2, 'dog': 1, 'DOG': 2, 'movie': 1, 'MOVIE': 2}
    c = sum(cs.get(e, 0) for e in events)
    # Return 'You need extra sleep' if coffee count exceeds 3
    return 'You need extra sleep' if c > 3 else c


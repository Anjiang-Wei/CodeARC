def solution(character, build):
    from itertools import accumulate

    CHARACTERS = {
        "warrior": (4, [11, 8, 12, 13, 13, 11, 9, 9]),
        "knight": (5, [14, 10, 10, 11, 11, 10, 9, 11]),
        "wanderer": (3, [10, 11, 10, 10, 14, 12, 11, 8]),
        "thief": (5, [9, 11, 9, 9, 15, 10, 12, 11]),
        "bandit": (4, [12, 8, 14, 14, 9, 11, 8, 10]),
        "hunter": (4, [11, 9, 11, 12, 14, 11, 9, 9]),
        "sorcerer": (3, [8, 15, 8, 9, 11, 8, 15, 8]),
        "pyromancer": (1, [10, 12, 11, 12, 9, 12, 10, 8]),
        "cleric": (2, [11, 11, 9, 12, 8, 11, 8, 14]),
        "deprived": (6, [11, 11, 11, 11, 11, 11, 11, 11]),
    }
    
    REQUIRED_SOULS = list(
        accumulate(
            [0, 0, 673, 690, 707, 724, 741, 758, 775, 793, 811, 829]
            + [
                round(pow(x, 3) * 0.02 + pow(x, 2) * 3.06 + 105.6 * x - 895)
                for x in range(12, 1000)
            ]
        )
    )

    starting_level, stats = CHARACTERS[character]
    delta = sum(b - s for b, s in zip(build, stats))
    level = starting_level + delta
    souls = REQUIRED_SOULS[level] - REQUIRED_SOULS[starting_level]
    
    return f"Starting as a {character}, level {level} will require {souls} souls."


def does_beast_match_dish(beast: str, dish: str) -> bool:
    return beast[0] == dish[0] and dish[-1] == beast[-1]


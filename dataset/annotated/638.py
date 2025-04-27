def check_bingo_winner(lst: list[int]) -> str:
    BINGO = {ord(c) - 64 for c in "BINGO"}
    # Check if the set of input numbers contains all numbers needed for "BINGO"
    return "WIN" if set(lst) >= BINGO else "LOSE"


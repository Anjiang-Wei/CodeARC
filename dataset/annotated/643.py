def calculate_switch_win_percentage(door: int, guesses: list[int]) -> int:
    # Calculate the number of participants who would win by switching
    wins_by_switching = len(guesses) - guesses.count(door)
    
    # Calculate the win percentage by switching
    win_percentage = 100.0 * wins_by_switching / len(guesses)
    
    # Return the rounded win percentage
    return round(win_percentage)


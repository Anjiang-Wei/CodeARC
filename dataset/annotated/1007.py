def count_correct_positions(correct_word: str, guess: str) -> int:
    if len(correct_word) != len(guess):
        raise Exception('Error')  # Raise an exception if the lengths are different
    # Count and return the number of characters that are in the correct position
    return sum(1 for c, g in zip(correct_word, guess) if c == g)


def calculate_punctuation_product(s: str) -> int:
    # Count the number of exclamation marks and question marks
    count_exclamations = s.count("!")
    count_questions = s.count("?")
    
    # Return the product of the counts
    return count_exclamations * count_questions


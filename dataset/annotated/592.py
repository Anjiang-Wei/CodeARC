def count_letter_occurrences(strng: str, letter: str) -> int:
    counter = 0
    
    for chr in strng:
        if chr == letter:
            counter += 1
    
    return counter


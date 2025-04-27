def generate_sorted_permutations(letters: dict[int, list[str]]) -> list[str]:
    from itertools import permutations
    
    # Create the word by repeating each character by its quantity
    word = "".join(qty * char for qty in letters for chars in letters[qty] for char in chars)
    
    # Generate all unique permutations and sort them
    return sorted({"".join(permutation) for permutation in permutations(word)})


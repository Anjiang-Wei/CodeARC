def replace_first_letters_with_number(phrase: str) -> str:
    SWAP = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}
    # Extract the first letter of each word and replace according to SWAP
    return ''.join(SWAP.get(word[0], word[0]) for word in phrase.split())


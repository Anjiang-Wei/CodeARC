def solution(text, key):
    import numpy as np
    from itertools import zip_longest
    from string import ascii_lowercase as lower, ascii_uppercase as upper

    # Create a dictionary to map each letter to its position in the alphabet
    D = {c: i % 26 for i, c in enumerate(lower + upper)}

    # Initialize the result list
    result = []

    # Remove non-alphabetic characters and convert text to uppercase
    text = ''.join(filter(str.isalpha, text)).upper()

    # Convert the key into a 2x2 matrix using the dictionary
    key_matrix = np.array(([D[key[0]], D[key[1]]], [D[key[2]], D[key[3]]]))

    # Process the text in pairs
    for c1, c2 in zip_longest(text[::2], text[1::2], fillvalue='Z'):
        # Multiply the key matrix by the text matrix
        x, y = key_matrix @ ([D[c1]], [D[c2]])
        # Append the encrypted characters to the result
        result.append(upper[x[0] % 26] + upper[y[0] % 26])

    # Return the encrypted message
    return ''.join(result)


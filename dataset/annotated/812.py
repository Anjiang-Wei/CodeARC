def find_sequence_values(val: int, k: int, col: str) -> list:
    # Initialize the dictionary and list for storing sequence values
    D, R = {}, [[], [], []]
    
    # Precompute the sequence values and categorize them by color
    for i in range(10000):
        D[i] = D.get(i - 1, 0) + i
        R[D[i] % 3].append(D[i])
    
    # Determine the index for the given color
    r = ['blue', 'red', 'yellow'].index(col)
    
    # Filter and return the first k terms greater than val
    return [e for e in R[r] if e > val][:k]


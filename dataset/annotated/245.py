def organize_elements_by_frequency(*arr: int) -> list[list[int] | None]:
    from collections import Counter
    
    # Count the frequency of each element in the array
    c = Counter(arr)
    
    # Create a dictionary where keys are frequencies and values are sorted lists of elements with that frequency
    c = {i: sorted([k for k, v in c.items() if v == i]) for i in c.values()}
    
    # Construct the output array with elements or None based on their frequency
    return [c[e] if e in c else None for e in range(len(arr) + 1)]


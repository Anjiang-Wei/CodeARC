def segregate_negatives_and_positives(values: list[int]) -> list[int]:
    i, j = 0, len(values) - 1

    while True:
        # Move i forward if the current number is negative
        while i < j and values[i] < 0:
            i += 1
        # Move j backward if the current number is positive
        while i < j and values[j] > 0:
            j -= 1
        # If pointers have crossed, the process is complete
        if i >= j:
            return values
        # Swap the misplaced positive and negative numbers
        values[i], values[j] = values[j], values[i]


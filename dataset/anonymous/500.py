def solution(usefulness, months):
    # Calculate the husband's total usefulness
    total_usefulness = sum(usefulness)
    
    # Calculate the woman's needs after exponential decay
    needs = 0.85**months * 100
    
    # Determine if the husband is useful enough
    return "Match!" if total_usefulness >= needs else "No match!"


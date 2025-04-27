def solution(tables, min_val, max_val):
    # Calculate the sum of the times tables
    return sum(tables) * (min_val + max_val) * (max_val - min_val + 1) // 2


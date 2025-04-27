def calculate_tables_sum(tables: list, min_val: int, max_val: int) -> int:
    # Calculate the sum of the times tables
    return sum(tables) * (min_val + max_val) * (max_val - min_val + 1) // 2


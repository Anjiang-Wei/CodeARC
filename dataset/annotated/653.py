def calculate_trees_on_perimeter(width: int, length: int, gaps: int) -> int:
    # Calculate the total number of positions for trees on the perimeter
    total_positions = 2 * width + 2 * length - 4
    
    # Calculate the number of trees and check if the layout is symmetrical
    num_trees, remainder = divmod(total_positions, gaps + 1)
    
    # If remainder is zero, the layout is symmetrical; otherwise, it's not
    return num_trees if remainder == 0 else 0


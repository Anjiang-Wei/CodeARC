def are_arm_strengths_equal(your_left: int, your_right: int, friends_left: int, friends_right: int) -> bool:
    # Check if both pairs of arms have the same strength when sorted
    return sorted([your_left, your_right]) == sorted([friends_left, friends_right])


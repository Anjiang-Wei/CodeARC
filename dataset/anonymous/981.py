def solution(your_left, your_right, friends_left, friends_right):
    # Check if both pairs of arms have the same strength when sorted
    return sorted([your_left, your_right]) == sorted([friends_left, friends_right])


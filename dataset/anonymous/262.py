def solution(archers):
    # Check if there are archers and all have at least 5 arrows
    return all(i >= 5 for i in archers) if archers else False


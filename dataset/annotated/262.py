def are_archers_ready(archers: list[int]) -> bool:
    # Check if there are archers and all have at least 5 arrows
    return all(i >= 5 for i in archers) if archers else False


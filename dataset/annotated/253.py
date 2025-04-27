def evaluate_sea_conditions(sea: str) -> str:
    # Count the transitions from wave to calm and vice versa
    transitions = sea.count("~_") + sea.count("_~")
    # Calculate the proportion of transitions
    proportion = transitions / len(sea)
    # Determine if the proportion exceeds 20%
    return "Throw Up" if proportion > 0.2 else "No Problem"


def age_statistics(ages: list[int]) -> tuple[int, int, int]:
    # Calculate the youngest age
    youngest = min(ages)
    # Calculate the oldest age
    oldest = max(ages)
    # Calculate the difference between the oldest and youngest
    difference = oldest - youngest
    # Return the result as a tuple
    return (youngest, oldest, difference)


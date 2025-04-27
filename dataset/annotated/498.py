def remaining_jumps_after_failures(failedCount: list[int]) -> int:
    t = 0
    for j in failedCount:
        t += 3  # Add 3 seconds for tidying up the rope after each failure
        if j + t > 60:
            # If the total time exceeds 60 seconds, calculate the remaining jumps
            return min(j, 60 - t + 3)
    # If no failure causes the time to exceed 60 seconds, return the remaining jumps
    return 60 - t


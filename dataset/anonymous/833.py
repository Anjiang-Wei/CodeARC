def solution(times):
    # Calculate the sum of all times
    total_sum = sum(times)
    # Find the minimum and maximum times
    min_time = min(times)
    max_time = max(times)
    # Calculate the average of the middle 3 times
    average_middle = (total_sum - (min_time + max_time)) / 3
    # Round the average to 2 decimal places
    average_rounded = round(average_middle, 2)
    # Return the average and the fastest time
    return (average_rounded, min_time)


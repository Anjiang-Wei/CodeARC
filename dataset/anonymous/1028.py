def solution(sum, difference):
    x = (sum + difference) / 2
    y = (sum - difference) / 2
    # Check for invalid conditions
    if sum < 0 or difference < 0 or x < 0 or y < 0:
        return None
    return (x, y)


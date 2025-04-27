def solution(n, m, speeds):
    lift, open, close, walk = speeds
    # Calculate time using the elevator
    elevator_time = abs(m - n) * lift + open + close + (n - 1) * lift + open
    # Calculate time by walking
    walking_time = (n - 1) * walk
    # Return the minimum of both times
    return min(elevator_time, walking_time)


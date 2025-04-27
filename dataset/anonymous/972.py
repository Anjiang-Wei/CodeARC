def solution(total_time, run_time, rest_time, speed):
    q, r = divmod(total_time, run_time + rest_time)
    # Calculate the total running time by multiplying the number of full cycles (q) by run_time
    # and adding the minimum of the remaining time (r) and run_time.
    return (q * run_time + min(r, run_time)) * speed


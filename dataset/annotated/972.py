def calculate_distance(total_time: int, run_time: int, rest_time: int, speed: int) -> int:
    q, r = divmod(total_time, run_time + rest_time)
    return (q * run_time + min(r, run_time)) * speed


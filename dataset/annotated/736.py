def calculate_sjf_total_time(jobs: list[int], index: int) -> int:
    return sum(j for i, j in enumerate(jobs) if j < jobs[index] or (j == jobs[index] and i <= index))


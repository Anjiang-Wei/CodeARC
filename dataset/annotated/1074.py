def calculate_completion_time(jobs: list[int], time_slice: int, target_index: int) -> int:
    total_cc = 0
    
    while True:
        for idx in range(len(jobs)):
            cc = min(jobs[idx], time_slice)
            jobs[idx] -= cc
            total_cc += cc
            # Check if the job at the given index is finished
            if idx == target_index and jobs[idx] == 0:
                return total_cc


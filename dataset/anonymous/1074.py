def solution(jobs, slice, index):
    total_cc = 0
    
    while True:
        for idx in range(len(jobs)):
            cc = min(jobs[idx], slice)
            jobs[idx] -= cc
            total_cc += cc
            # Check if the job at the given index is finished
            if idx == index and jobs[idx] == 0:
                return total_cc


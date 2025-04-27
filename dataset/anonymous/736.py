def solution(jobs, index):
    return sum(j for i, j in enumerate(jobs) if j < jobs[index] or (j == jobs[index] and i <= index))


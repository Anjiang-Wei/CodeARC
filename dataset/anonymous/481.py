def solution(bacteria, k):
    # Count bacteria that cannot be swallowed by any other bacteria
    return sum(1 for e in bacteria if not any(j for j in bacteria if e < j <= e + k))


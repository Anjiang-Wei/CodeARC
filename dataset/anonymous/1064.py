def solution(start, n, k):
    seq = []
    
    for step in range(k):
        seq.append(start)
        start = sum(int(dig) ** n for dig in str(start))
        
        if start in seq:
            cycle_start = seq.index(start)
            cycle = seq[cycle_start:]
            last_term = cycle[(k - cycle_start) % len(cycle)]
            return [cycle_start, cycle, len(cycle), last_term]
    
    return [0, [], 0, start]


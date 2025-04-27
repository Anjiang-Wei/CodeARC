def solution(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))


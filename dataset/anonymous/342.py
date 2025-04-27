def solution(m, n):
    return sum(i**j for i in range(m+1) for j in range(n+1))


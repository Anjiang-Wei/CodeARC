def solution(a, n):
    # Return the list with the nth element removed
    return a[:n] + a[n+1:]


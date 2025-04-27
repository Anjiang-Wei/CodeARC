def solution(a):
    a.sort()
    for i in range(1, len(a), 2):
        a[i], a[i-1] = a[i-1], a[i]
    # The function modifies the list in place and does not return anything.


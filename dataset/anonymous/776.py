def solution(A):
    A.sort(reverse=True)
    la = len(A)
    for i in range(la - 2):
        # Check if the three sides can form a triangle
        if A[i] < A[i + 1] + A[i + 2]:
            return A[i] + A[i + 1] + A[i + 2]
    return 0


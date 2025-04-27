def solution(L1, L2):
    sm, lg = sorted((L1, L2))
    # Calculate the maximum length for the three equal sticks
    return min(max(lg / 3, sm), lg / 2)


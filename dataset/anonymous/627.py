def solution(n, m):
    # Determine the final direction based on the grid dimensions
    return "LR"[n % 2] if m >= n else "UD"[m % 2]


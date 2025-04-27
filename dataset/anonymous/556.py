def solution(n):
    s = str(n)
    # Generate all possible numbers by removing one digit at a time
    return int(max(s[:i] + s[i+1:] for i in range(len(s))))


def solution(n):
    s = str(n)
    l = (len(s) - 1) // 2
    # Check if the number is balanced
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"


def solution(lst):
    return next((k for k in range(2, 1 + min(lst, default=1)) if all(n % k == 0 for n in lst)), 1)


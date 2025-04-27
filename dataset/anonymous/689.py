def solution(s):
    return max(sum(map(int, x)) for x in s.split('0'))


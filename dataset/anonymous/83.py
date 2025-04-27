from collections import defaultdict

def solution(s):
    n, count, sum = len(s), 0, 0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - i - 1]
        mp[sum - i - 1] += 1
    return count


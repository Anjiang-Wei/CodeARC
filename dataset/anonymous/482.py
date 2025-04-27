def solution(num):
    from collections import Counter
    
    s = [int(a) for a in str(num)]
    cnt = Counter(s)
    
    # Check if each digit matches the count of its index
    return all(cnt[i] == b for i, b in enumerate(s))


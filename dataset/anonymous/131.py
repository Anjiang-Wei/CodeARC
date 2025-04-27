def solution(arr): 
    pairs = [(a, b) for a in arr for b in arr if a != b]
    return max(pairs, key=lambda x: x[0] * x[1])


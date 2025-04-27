def solution(arr):
    if arr.count(0) > 1:
        return min(arr)
    
    neg = [n for n in arr if n < 0]
    pos = [n for n in arr if n >= 0]
    
    # If the number of negative numbers is odd
    if len(neg) % 2:
        # If zero is in the array, removing the smallest negative maximizes the product
        return min(neg) if 0 in arr else max(neg)
    else:
        # If the number of negative numbers is even, removing the smallest positive maximizes the product
        return min(pos) if pos else min(neg)


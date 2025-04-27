def solution(nums):
    from collections import Counter
    
    # Count occurrences of each number
    num_counts = Counter(nums)
    
    # Sum numbers that appear only once
    return sum(k for k, v in num_counts.items() if v == 1)


def solution(n):
    from collections import Counter
    
    # Convert the number to a string, then to a list of integers
    digits = [int(x) for x in str(n)]
    
    # Count occurrences of each digit
    digit_count = Counter(digits)
    
    # Check if any digit occurs as many times as its value
    return any(value == count for value, count in digit_count.items())


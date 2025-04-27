def solution(num):
    from collections import Counter
    
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    
    # Count the frequency of each digit
    digit_count = Counter(map(int, str(num)))
    
    # Check the number of digits with odd frequency
    odd_count = sum(1 for v in digit_count.values() if v % 2)
    
    # A number can be rearranged into a palindrome if at most one digit has an odd frequency
    return num > 10 and odd_count <= 1


def solution(string):
    if not string.isdigit() or not string:
        raise ValueError("Input must be a non-empty string of digits.")
    
    e0, b1 = len(string) // 2, (len(string) + 1) // 2
    
    # Calculate the sum of the first half and the second half
    left_sum = sum(map(int, string[:e0]))
    right_sum = sum(map(int, string[b1:]))
    
    # Check if the sums are equal
    return left_sum == right_sum


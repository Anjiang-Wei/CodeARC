def solution(n, index1, index2, digit):
    # Ensure the range is correctly defined regardless of the order of index1 and index2
    start, end = min(index1, index2), max(index1, index2)
    # Check if the digit exists in the specified range
    return str(digit) in str(n)[start:end+1]


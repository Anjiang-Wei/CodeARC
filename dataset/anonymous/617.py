def solution(s):
    """
    :type s: str
    :rtype: int
    """
    # Extract numbers from the string
    numbers = [int(i) for i in s.split() if i.isdigit()]
    
    # Determine the operation based on the presence of 'gains' or 'loses'
    if 'gains' in s.split():
        return sum(numbers)  # Perform addition
    else:
        return numbers[0] - numbers[1]  # Perform subtraction


def solution(code):
    # Calculate the sum of digits at odd positions multiplied by 1
    odd_sum = sum(map(int, code[0::2]))
    # Calculate the sum of digits at even positions multiplied by 3
    even_sum = sum(map(int, code[1::2])) * 3
    # Check if the total sum is divisible by 10
    return (odd_sum + even_sum) % 10 == 0


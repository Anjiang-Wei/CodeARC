def solution(card):
    # Remove spaces and convert to a list of integers
    s = list(map(int, card.replace(' ', '')))
    
    # Double every second digit from the right and adjust if necessary
    s[-2::-2] = [d * 2 - 9 if d * 2 > 9 else d * 2 for d in s[-2::-2]]
    
    # Check if the sum of the digits is divisible by 10
    return sum(s) % 10 == 0


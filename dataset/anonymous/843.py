def solution(value):
    s = f'0{value:b}'  # Convert to binary with leading zero
    i = s.rfind('01')  # Find the rightmost '01'
    # Swap '01' to '10' and sort the rest to get the smallest number
    s = s[:i] + '10' + ''.join(sorted(s[i+2:]))
    return int(s, 2)  # Convert back to integer


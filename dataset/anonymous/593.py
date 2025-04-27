def solution(num):
    prev = 0
    out = ''

    for dig in str(num):
        # Check if both current and previous digits are odd or even and not zero
        if int(dig) % 2 == int(prev) % 2 and int(prev) and int(dig):
            out += '*-'[int(prev) % 2]  # Add '*' for even, '-' for odd
        out += dig
        prev = dig
    return out


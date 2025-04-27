def solution(_str):
    def digit_sum(x):
        # Calculate the sum of digits of the number
        return sum(int(c) for c in x)
    
    # Split the string into numbers, sort by digit sum, then by string value
    return ' '.join(sorted(sorted(_str.split()), key=digit_sum))


def solution(a, b):
    def is_even(x):
        # Check if all digits in the number are even
        return all(int(i) % 2 == 0 for i in str(x))
    
    # Calculate the range of numbers to check
    first = int(a ** 0.5) + 1
    last = int(b ** 0.5) + 1
    
    # Find and return all even-digit perfect squares in the range
    return sorted([x * x for x in range(first, last) if is_even(x * x)])


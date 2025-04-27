def count_fibonacci_digit_occurrences(n: int) -> list[tuple[int, int]]:
    from collections import Counter

    def fibonacci(n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def count_digits(num: int) -> Counter:
        return Counter(str(num))

    fib_number = fibonacci(n)
    digit_count = count_digits(fib_number)
    
    # Create a list of tuples (count, digit) and sort in descending order
    result = sorted(((count, int(digit)) for digit, count in digit_count.items()), reverse=True)
    
    return result


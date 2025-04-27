def solution(n):
    def loneliest(n):
        a = list(map(int, str(n)))
        # Calculate loneliness for each digit
        b = [(sum(a[max(0, i - x):i + x + 1]) - x, x) for i, x in enumerate(a)]
        # Check if there's a '1' with minimal loneliness
        return (min(b)[0], 1) in b

    return loneliest(n)


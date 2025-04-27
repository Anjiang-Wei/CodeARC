def solution(n):
    from bisect import bisect

    # Precompute the sum of squares of digits for numbers 0-9
    sum_dig = lambda n, D={str(d): d*d for d in range(10)}: sum(map(D.get, str(n)))

    # Recursive function to determine if a number is happy
    def is_happy(n):
        return n > 4 and is_happy(sum_dig(n)) or n == 1

    # Precompute happy numbers up to 300,000
    happy_set = set(filter(is_happy, range(100)))
    for num in range(100, 3 * 10 ** 5):
        if sum_dig(num) in happy_set:
            happy_set.add(num)

    # Sort the happy numbers for efficient searching
    happy_list = sorted(happy_set)

    # Return the list of happy numbers up to n
    return happy_list[:bisect(happy_list, n)]


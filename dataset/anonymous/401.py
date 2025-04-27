def solution(input):
    # Count the number of characters with odd occurrences
    # A string can be permuted to form a palindrome if at most one character has an odd count
    return sum(input.count(c) % 2 for c in set(input)) < 2


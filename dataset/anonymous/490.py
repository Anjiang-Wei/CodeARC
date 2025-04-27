def solution(first, second):
    first = first.lower()
    second = second.lower()

    for i in range(len(first) - 1):  # Check pairs of characters
        if first[i:i+2] in second:
            return True
    return False


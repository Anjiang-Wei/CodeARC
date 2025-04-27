def solution(l):
    l = l[:]  # Create a copy of the list to avoid mutating the input
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]  # Swap if the current element is greater than the next
    return l  # Return the list after one complete pass


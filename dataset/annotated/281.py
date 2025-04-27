def split_and_rearrange(s: str) -> list[str]:
    l1 = list(s)
    l2 = []
    l3 = []
    while len(l1) > 1:
        l2.append(l1.pop())  # Remove the last character and add to l2
        l3.append(l1.pop(0))  # Remove the first character and add to l3
    return ["".join(l2), "".join(l3), "".join(l1)]  # Return the three strings


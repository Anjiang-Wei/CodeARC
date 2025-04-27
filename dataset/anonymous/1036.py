def solution(seq):
    # Convert the sequence to a single string and find unique digits
    return len(set(''.join(seq)))


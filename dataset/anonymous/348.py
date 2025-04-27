def solution(seq):
    # Calculate the expected sum of the arithmetic progression
    expected_sum = (min(seq) + max(seq)) * (len(seq) + 1) / 2
    # Calculate the actual sum of the given sequence
    actual_sum = sum(seq)
    # The missing term is the difference between the expected and actual sums
    return expected_sum - actual_sum


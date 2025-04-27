def solution(arr):
    nTerms = ((1 + 8 * len(arr)) ** 0.5 - 1) / 2
    # Check if the array length is greater than 1 and nTerms is an integer
    if len(arr) > 1 and nTerms.is_integer():
        # Calculate sums for each segment and check if all are equal
        sums = {sum(arr[int(i * (i + 1) // 2):int(i * (i + 1) // 2) + i + 1]) for i in range(int(nTerms))}
        return len(sums) == 1
    return False


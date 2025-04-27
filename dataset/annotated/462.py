def find_numbers_with_constraints(nMax: int, maxSum: int) -> list[int]:
    def check(num: int, max_sum: int) -> bool:
        # Convert number to list of digits
        l = [int(i) for i in str(num)]
        # Check sum of every four consecutive digits
        for i in range(0, len(l) - 3):
            if sum(l[i:i+4]) > max_sum:
                return False
        return True

    # Find all numbers satisfying the condition
    found = [i for i in range(1000, nMax + 1) if check(i, maxSum)]
    
    # Calculate mean of found numbers
    mean_value = sum(found) / float(len(found))
    
    # Find the closest number to the mean
    closest = min(found, key=lambda x: (abs(x - mean_value), x))
    
    # Return the result as a list
    return [len(found), closest, sum(found)]


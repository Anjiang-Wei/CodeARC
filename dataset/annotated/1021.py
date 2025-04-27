def max_product_of_three(nums: list[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    import heapq
    # Find the three largest numbers and two smallest numbers
    largest_three = heapq.nlargest(3, nums)
    smallest_two = heapq.nsmallest(2, nums)
    # Calculate the maximum product of three numbers
    return max(largest_three[0] * largest_three[1] * largest_three[2], 
               largest_three[0] * smallest_two[0] * smallest_two[1])


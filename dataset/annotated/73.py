def count_odd_digit_numbers(nums: list[int]) -> int:
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    count_odd_digit_numbers([15, -73, 14, -15]) => 1 
    count_odd_digit_numbers([33, -2, -3, 45, 21, 109]) => 2
    """

    ans, odd = 0, ["1", "3", "5", "7", "9"]
    for num in nums:
        if num > 10 and str(num)[0] in odd and str(num)[-1] in odd:
            ans += 1
    return ans


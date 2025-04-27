def solution(nums):
  first_odd = next((el for el in nums if el % 2 != 0), None)
  return first_odd


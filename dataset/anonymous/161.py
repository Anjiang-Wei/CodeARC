def solution(str1):
  for index, c in enumerate(str1):
    if str1[:index + 1].count(c) > 1:
      return c
  return None


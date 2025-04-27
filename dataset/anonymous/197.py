def solution(test_str):
  return tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))


def solution(test_tup):
  return tuple(i * j for i, j in zip(test_tup, test_tup[1:]))


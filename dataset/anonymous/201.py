def solution(test_tup):
  return tuple(e for e in test_tup if not isinstance(e, tuple))


def solution(numbers):
  sorted_set = sorted(set(numbers))
  if len(sorted_set) < 2:
    return None
  return sorted_set[1]


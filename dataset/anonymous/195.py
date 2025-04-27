from itertools import combinations

def solution(test_list):
  return [tuple(map(sum, zip(*t))) for t in combinations(test_list, 2)]


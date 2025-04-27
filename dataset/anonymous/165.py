def solution(test_str):
  num_str = ''.join(i for i in test_str if i.isdigit())
  else_str = ''.join(i for i in test_str if not i.isdigit())
  return else_str + num_str


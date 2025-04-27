def parse_string_to_tuple(test_str: str) -> tuple[int, ...]:
  return tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))


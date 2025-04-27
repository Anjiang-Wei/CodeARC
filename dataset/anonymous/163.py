import re

def solution(text, pattern):
  match = re.search(pattern, text)
  if match is None:
    return None
  s = match.start()
  e = match.end()
  return (match.re.pattern, s, e)


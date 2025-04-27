def solution(str, name):
    it = iter(str.lower())
    # Check if all characters in 'name' are in 'str' in order
    return all(c in it for c in name.lower())


def solution(lst):
    m = min(lst, key=abs)
    # Check if the closest value to zero is unique
    return m if m == 0 or -m not in lst else None


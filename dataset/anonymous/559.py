def solution(items, index, default_value):
    try:
        return items[index]
    except IndexError:
        return default_value


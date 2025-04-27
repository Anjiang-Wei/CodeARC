def solution(data):
    if isinstance(data, (int, str, float)):
        return type(data)(str(data)[::-1])
    return data


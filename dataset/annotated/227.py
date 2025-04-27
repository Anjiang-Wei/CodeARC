def reverse_if_primitive(data: int | str | float | list | dict) -> int | str | float | list | dict:
    if isinstance(data, (int, str, float)):
        return type(data)(str(data)[::-1])
    return data


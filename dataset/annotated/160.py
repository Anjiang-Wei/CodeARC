def is_armstrong_number(number: int) -> bool:
    order = len(str(number))
    return sum([int(i) ** order for i in str(number)]) == number


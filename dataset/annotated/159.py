def calculate_even_odd_difference(list1: list[int]) -> int:
    first_even = next((el for el in list1 if el % 2 == 0), -1)
    first_odd = next((el for el in list1 if el % 2 != 0), -1)
    return first_even - first_odd


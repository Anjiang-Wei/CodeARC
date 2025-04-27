def find_pandigital_numbers(offset: int, size: int, start: int = 1023456789) -> list[int]:
    def is_pandigital(num: int) -> bool:
        # Check if the number is pandigital
        num_str = str(num)
        return num_str[0] != '0' and len(set(num_str)) == 10

    pandigital_numbers = []
    for i in range(max(start, offset), 9876543211):
        if is_pandigital(i):
            pandigital_numbers.append(i)
            if len(pandigital_numbers) == size:
                break

    return pandigital_numbers


def solution(offset, size, start=1023456789):
    def is_pandigital(num):
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


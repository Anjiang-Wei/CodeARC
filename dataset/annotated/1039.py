def add_binary_strings(a: str, b: str) -> str:
    def binary_string_to_int(string: str) -> int:
        # Convert binary string to integer without using built-in conversion
        return sum((d == '1') * 2**i for i, d in enumerate(string[::-1]))
    
    # Calculate the sum of the two binary numbers and format it as a binary string
    return '{:b}'.format(binary_string_to_int(a) + binary_string_to_int(b))


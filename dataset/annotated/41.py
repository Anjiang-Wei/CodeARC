def is_string_length_prime(string: str) -> bool:
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    is_string_length_prime('Hello') == True
    is_string_length_prime('abcdcba') == True
    is_string_length_prime('kittens') == True
    is_string_length_prime('orange') == False
    """

    def is_prime(a: int) -> bool:
        return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

    return is_prime(len(string))


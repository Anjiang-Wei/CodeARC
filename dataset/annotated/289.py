def next_palindrome_number(val: int) -> int:
    def is_palindrome(n: int) -> bool:
        s = str(n)
        return s == s[::-1]

    val += 1
    while not is_palindrome(val):
        val += 1
    return val


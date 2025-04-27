def is_rotated_palindrome(s: str) -> bool:
    return s in (s + s)[1:-1]


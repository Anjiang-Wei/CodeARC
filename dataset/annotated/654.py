def find_palindrome(num: int) -> int:
    if type(num) is not int or num < 0:
        return "Not valid"
    
    def is_pal(n: int) -> bool:
        # Check if the number is greater than 10 and is a palindrome
        return n > 10 and n == int(str(n)[::-1])
    
    c = 0
    for i in range(num, num**2):
        if is_pal(i):
            return i
        elif is_pal(i - c):
            return i - c
        else:
            c += 2


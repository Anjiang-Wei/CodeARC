def square_and_concatenate_digits(num: int) -> int:
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)


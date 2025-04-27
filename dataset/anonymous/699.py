def solution(n):
    tr = str.maketrans('56789', '45678')
    # Translate the number according to the faulty odometer rules and convert from base 9
    return int(str(n).translate(tr), 9)


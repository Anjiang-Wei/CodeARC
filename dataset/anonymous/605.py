def solution(xA, xB, xC):
    a, b, c = list(map(float, [xA, xB, xC]))
    # Calculate the harmonic conjugate point D using the given formula
    d = ((a * c) + (b * c) - (2 * a * b)) / (2 * c - a - b)
    # Return the result rounded to four decimal places
    return round(d, 4)


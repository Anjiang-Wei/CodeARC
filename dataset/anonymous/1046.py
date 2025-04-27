def solution(number):
    def summ(number, d):
        n = (number - 1) // d
        return n * (n + 1) * d // 2

    # Calculate the sum of multiples of 3 and 5, subtracting the multiples of 15 to avoid double counting
    return summ(number, 3) + summ(number, 5) - summ(number, 15)


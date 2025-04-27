def are_amicable_numbers(num1: int, num2: int) -> bool:
    def getDivs(n: int) -> set:
        # Calculate proper divisors of n
        return {1} | {y for x in range(2, int(n**0.5) + 1) for y in [n // x, x] if n % x == 0}

    # Check if num1 and num2 are amicable numbers
    return sum(getDivs(num1)) == num2 and sum(getDivs(num2)) == num1


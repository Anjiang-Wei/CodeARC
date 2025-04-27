def solution(salary, bonus):
    # Calculate the total salary based on the bonus condition
    total_salary = salary * (10 if bonus else 1)
    # Return the total salary as a string prefixed with "$"
    return "${}".format(total_salary)


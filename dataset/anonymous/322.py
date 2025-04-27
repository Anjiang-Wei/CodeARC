def solution(stg, value, happiness):
    sabbatical = (value + happiness + sum(1 for c in stg if c in "sabbatical")) > 22
    # Check if the sum of value, happiness, and the count of specific letters is greater than 22
    return "Sabbatical! Boom!" if sabbatical else "Back to your desk, boy."


def solution(subtotal, tax, tip):
    # Calculate the total by adding tax and tip to the subtotal
    # Tax and tip are percentages, so divide by 100
    # Round the result to two decimal places
    return round(subtotal * (1 + tax / 100.0 + tip / 100.0), 2)


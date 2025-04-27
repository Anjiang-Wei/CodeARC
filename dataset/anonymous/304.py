def solution(num):
    # Format the number with commas and round to 3 decimal places
    formatted_number = "{:,.3f}".format(num)
    # Remove trailing zeros and the decimal point if necessary
    return formatted_number.rstrip("0").rstrip(".")


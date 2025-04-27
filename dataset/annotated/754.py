def calculate_original_price(discounted_price: float, sale_percentage: float) -> float:
    # Calculate the original price using the formula:
    # original_price = discounted_price / (1 - sale_percentage / 100)
    # Round the result to two decimal places
    return round(discounted_price / ((100 - sale_percentage) * 0.01), 2)


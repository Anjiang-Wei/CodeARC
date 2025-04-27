def calculate_bottles_needed(price: float, discount: float, holiday_cost: float) -> int:
    # Calculate the saving per bottle
    saving = price * discount / 100.0
    # Calculate and return the number of bottles needed to cover the holiday cost
    return int(holiday_cost / saving)


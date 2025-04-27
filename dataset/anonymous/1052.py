def solution(price, discount, holiday_cost):
    # Calculate the saving per bottle
    saving = price * discount / 100.0
    # Calculate and return the number of bottles needed to cover the holiday cost
    return int(holiday_cost / saving)


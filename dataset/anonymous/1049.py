def solution(litres, price_per_litre):
    # Calculate the discount based on the number of litres
    discount = int(min(litres, 10) / 2) * 5 / 100
    # Calculate the total cost with the discount applied and round to 2 decimal places
    total_cost = round((price_per_litre - discount) * litres, 2)
    return total_cost


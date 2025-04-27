def is_disarium_number(n: int) -> str:
    # Calculate the sum of digits powered with their respective positions
    disarium_sum = sum(int(d)**i for i, d in enumerate(str(n), 1))
    # Check if the sum equals the original number
    return "Disarium !!" if n == disarium_sum else "Not !!"


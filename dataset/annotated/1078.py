def calculate_total_price(name: str, price: int = 30) -> int:
    return sum(price for _ in name)


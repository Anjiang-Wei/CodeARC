def calculate_box_properties(w: float, h: float, d: float) -> list[float]:
    area = 2 * (w * h + h * d + w * d)
    volume = w * h * d
    return [area, volume]


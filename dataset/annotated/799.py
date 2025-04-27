def calculate_crates_from_dimensions(length: int, width: int, height: int) -> int:
    # Convert dimensions from feet to inches and calculate the number of crates
    return (length * 12 // 16) * (width * 12 // 16) * (height * 12 // 16)


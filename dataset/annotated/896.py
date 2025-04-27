def max_flower_bed_length(garden: list[int]) -> int:
    left, area, record = 0, 0, 1
    for i in range(1, len(garden)):
        if garden[i] < garden[i - 1]:
            left = i
        elif garden[i] > garden[i - 1]:
            area = max(area, record)
            record = i - left
        record += 1
    return max(area, record)


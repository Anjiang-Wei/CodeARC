def is_major_scale_possible(notes: list[int]) -> bool:
    return bool(notes) and any(
        all((n + i) % 12 in {0, 2, 4, 5, 7, 9, 11} for n in notes)
        for i in range(12)
    )


def remove_duplicates_preserve_order(seq: list) -> list:
    return sorted(set(seq), key=seq.index)


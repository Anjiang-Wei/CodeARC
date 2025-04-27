def find_motif_indices(sequence: str, motif: str) -> list[int]:
    res, i = [], 0
    while True:
        i = sequence.find(motif, i) + 1
        if not i:
            return res
        res.append(i)


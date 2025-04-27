def replace_exclamation_question_pairs(s: str) -> str:
    from itertools import groupby

    # Create a run-length encoding of the string
    rle = [[i, k, len(list(g))] for i, (k, g) in enumerate(groupby(s))]
    queue = {}

    # Populate the queue with indices of each character group
    for i, k, l in reversed(rle):
        if l not in queue:
            queue[l] = {}
        queue[l].setdefault(k, []).append(i)

    # Replace pairs of '!' and '?' with spaces
    for l in queue:
        while sum(map(bool, queue[l].values())) > 1:
            for c in queue[l]:
                rle[queue[l][c].pop()][1] = ' '

    # Reconstruct the string from the modified run-length encoding
    return ''.join(k * l for i, k, l in rle)


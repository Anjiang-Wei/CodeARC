def is_reverse_complement_contained(seq1: str, seq2: str) -> bool:
    if len(seq1) < len(seq2):
        seq1, seq2 = seq2, seq1
    # Reverse seq2 and replace with complementary bases
    seq2 = seq2[::-1].replace('C', 'g').replace('G', 'c').replace('T', 'a').replace('A', 't').upper()
    # Check if seq2 is a substring of seq1
    return seq1.find(seq2) >= 0


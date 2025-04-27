def solution(dna):
    import re

    # Transcription table
    TABLE = str.maketrans('ACGT', 'UGCA')

    # Codon to amino acid mapping
    CODON_DICT = {
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
        'AAA': 'Lys', 'AAG': 'Lys',
        'AAU': 'Asn', 'AAC': 'Asn',
        'AUG': 'Met',
        'GAU': 'Asp', 'GAC': 'Asp',
        'UUU': 'Phe', 'UUC': 'Phe',
        'UGU': 'Cys', 'UGC': 'Cys',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'CAA': 'Gln', 'CAG': 'Gln',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'AGU': 'Ser', 'AGC': 'Ser',
        'GAA': 'Glu', 'GAG': 'Glu',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
        'UGG': 'Trp',
        'CAU': 'His', 'CAC': 'His',
        'UAU': 'Tyr', 'UAC': 'Tyr',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'UAG': 'Stop', 'UGA': 'Stop', 'UAA': 'Stop'
    }

    # Transcribe DNA to RNA
    rna = re.findall(r'.{1,3}', dna.translate(TABLE))
    # Translate RNA to polypeptide
    polypeptide = ' '.join(x for x in map(CODON_DICT.get, rna) if x)

    return ' '.join(rna), polypeptide


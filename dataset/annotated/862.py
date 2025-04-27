def generate_wave_histogram(waves: list[int]) -> str:
    m = max(waves)
    # Create the histogram with '■' for waves and '□' for blanks
    rotHist = [('■' * v).rjust(m, '□') for v in waves]
    # Transpose the histogram to draw from bottom to top
    return '\n'.join(map(''.join, zip(*rotHist)))


def correct_parity_error(m: int, n: int, bits: str) -> str:
    l = m * n
    
    # Find the row with incorrect parity
    row = next((i for i in range(m) if (bits[i*n:(i+1)*n] + (bits[l+i] if l+i < len(bits) else "")).count("1") % 2), None)
    
    # Find the column with incorrect parity
    col = next((i for i in range(n) if (''.join(bits[j*n + i] for j in range(m)) + (bits[l+m+i] if l+m+i < len(bits) else "")).count("1") % 2), None)

    # If no errors are found, return the original bits
    if row is None and col is None:
        return bits
    
    # Determine the position of the error
    if row is not None and col is not None:
        err = row * n + col  # Error in data bits
    elif row is not None:
        err = l + row  # Error in row parity bit
    else:
        err = l + m + col  # Error in column parity bit
    
    # Correct the error by flipping the bit
    corrected_bits = bits[:err] + str(1 - int(bits[err])) + bits[err+1:] if err < len(bits) else bits
    
    return corrected_bits

def solution(B, Jmin, Jmax):
    # Check if B is positive and Jmin is less than or equal to Jmax
    if B > 0 and Jmin <= Jmax:
        # Calculate energies for each J from Jmin to Jmax
        return [B * J * (J + 1) for J in range(Jmin, Jmax + 1)]
    # Return empty array if conditions are not met
    return []


def determine_membership_level(amount: float, platinum: float, gold: float, silver: float, bronze: float) -> str:
    ordered = reversed(sorted((v, k) for k, v in locals().items() if k != 'amount'))
    return next((level.capitalize() for threshold, level in ordered if amount >= threshold), 'Not a member')


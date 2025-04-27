def solution(amount, platinum, gold, silver, bronze):
    ordered = reversed(sorted((v, k) for k, v in locals().items() if k != 'amount'))
    return next((level.capitalize() for threshold, level in ordered if amount >= threshold), 'Not a member')


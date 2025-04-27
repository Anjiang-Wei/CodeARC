def calculate_amortization_schedule(rate: float, bal: float, term: int, num_payments: int) -> str:
    monthlyRate = rate / (12 * 100)
    c = bal * (monthlyRate * (1 + monthlyRate) ** term) / (((1 + monthlyRate) ** term) - 1)
    newBalance = bal
    princ = 0
    interest = 0
    for i in range(num_payments):
        interest = newBalance * monthlyRate
        princ = c - interest
        newBalance -= princ
    return 'num_payment %d c %.0f princ %.0f int %.0f balance %.0f' % (num_payments, c, princ, interest, newBalance)


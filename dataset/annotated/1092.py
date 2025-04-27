def extract_phone_number(s: str) -> str:
    from collections import Counter

    EXECUTIONS_ORDER = [
        ('Z', Counter("ZERO"), '0'),
        ('W', Counter("TWO"), '2'),
        ('U', Counter("FOUR"), '4'),
        ('X', Counter("SIX"), '6'),
        ('G', Counter("EIGHT"), '8'),
        ('O', Counter("ONE"), '1'),
        ('H', Counter("THREE"), '3'),
        ('F', Counter("FIVE"), '5'),
        ('V', Counter("SEVEN"), '7'),
        ('I', Counter("NINE"), '9')
    ]

    ans, count, executions = [], Counter(s), iter(EXECUTIONS_ORDER)
    while count:
        c, wordCount, value = next(executions)
        ans.extend([value] * count[c])
        for _ in range(count[c]):
            count -= wordCount
    return ''.join(sorted(ans))


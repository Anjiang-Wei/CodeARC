def solution(*args):
    from itertools import zip_longest
    # Use zip_longest to interlace strings, filling with empty strings when one runs out
    return ''.join(''.join(x) for x in zip_longest(*args, fillvalue=''))


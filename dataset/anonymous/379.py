def solution(meme):
    import re
    from itertools import accumulate

    patterns = [
        (re.compile('.*'.join('bug'), flags=re.I), 'Roma'),
        (re.compile('.*'.join('boom'), flags=re.I), 'Maxim'),
        (re.compile('.*'.join('edits'), flags=re.I), 'Danik'),
    ]

    # Iterate over accumulated characters in the meme
    # Check each pattern to find the earliest match
    return next((who for m in accumulate(meme) for pattern, who in patterns if pattern.search(m)), 'Vlad')


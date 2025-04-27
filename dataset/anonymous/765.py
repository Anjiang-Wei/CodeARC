def solution(*words):
    from itertools import groupby
    from operator import itemgetter
    from os.path import commonprefix

    # Filter out empty words
    words = [w for w in words if w]
    result = {}

    # Group words by their first character
    for key, grp in groupby(sorted(words), key=itemgetter(0)):
        lst = list(grp)
        # Find the common prefix
        prefix = commonprefix(lst)
        # Recursively build the tree for the remaining parts of the words
        result[prefix] = {w[len(prefix):] for w in lst if w[len(prefix):]}
        
        # Recursively call to handle nested words
        result[prefix] = solution(*result[prefix])
        
    return result


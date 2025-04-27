def solution(dna):
    def pairs_to_dict(pairs):
        d = {}
        for pair in pairs:  # Add two replacing rules for each pair
            d[pair[0]] = pair[1]
            d[pair[1]] = pair[0]
        return d

    pairs = [("A", "T"), ("C", "G")]
    replacing_rules = pairs_to_dict(pairs)
    return "".join([replacing_rules[a] for a in dna])


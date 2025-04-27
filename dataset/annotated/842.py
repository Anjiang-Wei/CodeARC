def split_number_to_components(n: str) -> list[str]:
    def split_exp(n: str) -> list[str]:
        dot = n.find('.')
        if dot == -1: 
            dot = len(n)
        # Create a list of numbers with one nonzero digit
        return [d + "0" * (dot - i - 1) if i < dot else ".{}{}".format("0" * (i - dot - 1), d)
                for i, d in enumerate(n) if i != dot and d != '0']
    
    return split_exp(n)


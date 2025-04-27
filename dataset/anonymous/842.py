def solution(n):
    def split_exp(n):
        dot = n.find('.')
        if dot == -1: 
            dot = len(n)
        # Create a list of numbers with one nonzero digit
        return [d + "0" * (dot - i - 1) if i < dot else ".{}{}".format("0" * (i - dot - 1), d)
                for i, d in enumerate(n) if i != dot and d != '0']
    
    return split_exp(n)


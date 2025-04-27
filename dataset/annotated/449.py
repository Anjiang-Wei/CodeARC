def mutate_chromosome(chromosome: str, p: float) -> str:
    from random import random
    
    def mutate(chromosome, p):
        res = ''
        for s in chromosome:
            # Flip the bit with probability p
            res += str(1 - int(s)) if random() < p else s
        return res
    
    return mutate(chromosome, p)


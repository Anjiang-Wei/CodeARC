def solution(a, b):
    def swap_case_based_on_count(s, ref):
        # Swap case of characters in s based on their count in ref
        return [char if ref.lower().count(char.lower()) % 2 == 0 else char.swapcase() for char in s]
    
    new_a = swap_case_based_on_count(a, b)
    new_b = swap_case_based_on_count(b, a)
    
    return ''.join(new_a) + ''.join(new_b)


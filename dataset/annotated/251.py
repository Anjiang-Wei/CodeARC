def swap_case_by_reference_count(a: str, b: str) -> str:
    def swap_case_based_on_count(s: str, ref: str) -> list[str]:
        # Swap case of characters in s based on their count in ref
        return [char if ref.lower().count(char.lower()) % 2 == 0 else char.swapcase() for char in s]
    
    new_a = swap_case_based_on_count(a, b)
    new_b = swap_case_based_on_count(b, a)
    
    return ''.join(new_a) + ''.join(new_b)


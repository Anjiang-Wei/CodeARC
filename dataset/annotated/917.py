from typing import List, Any

def sort_mixed_array(array: List[Any]) -> List[Any]:
    def custom_sort_key(x: Any):
        # Check if the element is a digit
        is_digit = str(x).isdigit()
        # Determine if the element is an integer
        is_int = isinstance(x, int)
        # Return a tuple for sorting: (is_digit, string_representation, negative is_int)
        return (is_digit, str(x), -is_int)
    
    # Sort the array using the custom key
    return sorted(array, key=custom_sort_key)


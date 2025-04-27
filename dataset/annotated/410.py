def split_even_numbers(numbers: list[int], split_type: int) -> list[int]:
    result = []
    
    for a in numbers:
        if a % 2:
            result.append(a)
        else:
            # Generate pairs of odd numbers that sum to the even number
            pairs = [(b, a - b) for b in range(1, a // 2 + 1, 2) if (a - b) % 2]
            
            if split_type == 0:
                # Closest odd numbers
                result.extend(pairs[-1])
            elif split_type == 1:
                # Most distant odd numbers
                result.extend(pairs[0])
            elif split_type == 2:
                # Maximum possible equal odd numbers
                for c, _ in reversed(pairs):
                    quo, rem = divmod(a, c)
                    if not rem:
                        result.extend([c] * quo)
                        break
            elif split_type == 3:
                # Split into 1s
                result.extend([1] * a)
    
    return result


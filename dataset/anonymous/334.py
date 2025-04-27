def solution(signature, indexes, n):
    from collections import deque
    
    fib = deque(signature)
    for _ in range(n):
        # Calculate the next number in the sequence using the specified indexes
        fib.append(sum(map(fib.__getitem__, indexes)))
        # Remove the oldest number to maintain the sequence length
        fib.popleft()
    
    # Return the nth element in the sequence
    return fib[0]


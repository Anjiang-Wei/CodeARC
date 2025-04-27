def solution(m):
    def even_fib_sum(max_value):
        x, y = 0, 1
        counter = 0
        while y < max_value:
            if y % 2 == 0:
                counter += y
            x, y = y, x + y
        return counter
    
    return even_fib_sum(m)


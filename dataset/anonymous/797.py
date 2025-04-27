def solution(num):
    def consecutive_sum(num):
        upper_limit = 1
        while True:
            if upper_limit * (upper_limit + 1) // 2 > num:
                break
            upper_limit += 1
        
        # Calculate the number of valid n values
        return sum(
            1 if i % 2 and not num % i else 1 if not i % 2 and num % i == i // 2 else 0 
            for i in range(1, upper_limit)
        )
    
    return consecutive_sum(num)


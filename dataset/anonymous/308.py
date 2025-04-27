def solution(n, z):
    def subsets(collection):
        if len(collection) == 1:
            yield [collection]
            return

        first = collection[0]
        for smaller in subsets(collection[1:]):
            yield [first] + smaller
            for i, subset in enumerate(smaller):
                yield smaller[:i] + [first + subset] + smaller[i+1:]

    def bucket_digit_distributions_total_sum(n):
        # Calculate the sum of all possible bucket distributions
        return sum(sum(map(int, sub)) for sub in subsets(str(n))) - n

    f_nf = bucket_digit_distributions_total_sum(n) + z
    while True:
        n += 1
        if bucket_digit_distributions_total_sum(n) > f_nf:
            return n


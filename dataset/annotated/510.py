def sequence_analysis(n: int, k: int = None, mode: str = 'length_sup_u_k') -> int:
    from itertools import islice, count

    def u1():
        a = {1: 1, 2: 1}
        yield a[1]
        yield a[2]
        for n in count(3):
            a[n] = a[n - a[n - 1]] + a[n - a[n - 2]]
            yield a[n]

    if mode == 'length_sup_u_k':
        # Count terms u[i] >= k for 1 <= i <= n
        return len(list(filter(lambda x: x >= k, islice(u1(), 1, n))))
    elif mode == 'comp':
        # Count terms where u[i] < u[i-1] for 1 <= i <= n
        return sum(k1 < k0 for k0, k1 in zip(list(islice(u1(), 1, n)), list(islice(u1(), 2, n))))


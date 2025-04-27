def calculate_number_of_bricks(k: int, n: int, m: int, x: int) -> int:
    def simulate_building(k: int, n: int, p: int) -> int:
        r = [(k, k, 0), (k, p, p)]
        for i in range(n - 2):
            u, d = r[0][1] + r[1][1], r[1][1]
            r = [r[1], (r[1][0] + u - d, u, d)]
        return r[1][0]

    z, o = simulate_building(k, n - 1, 0), simulate_building(k, n - 1, 1)
    return simulate_building(k, x, (m - z) // (o - z))


def generate_random_value(seed: int, action: str, *args: int) -> tuple:
    import hashlib

    HASH_MAX = (1 << 32 * 4) - 1

    def random(seed: int) -> tuple:
        x = int(hashlib.md5(str(seed).encode()).hexdigest(), 16)
        seed += 1
        return x / HASH_MAX, seed

    def randint(seed: int, start: int, end: int) -> tuple:
        rand_value, new_seed = random(seed)
        return start + int(rand_value * (end + 1 - start)), new_seed

    if action == "random":
        rand_value, new_seed = random(seed)
        return rand_value, new_seed
    elif action == "randint":
        start, end = args
        rand_int, new_seed = randint(seed, start, end)
        return rand_int, new_seed
    else:
        raise ValueError("Invalid action")


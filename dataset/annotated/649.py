def zombie_apocalypse(zombies: int, distance: float, ammo: int) -> str:
    def zombie_shootout(zombies: int, distance: float, ammo: int, shot: int = 0) -> str:
        if not zombies:
            return f'You shot all {shot} zombies.'
        if distance <= 0:
            return f'You shot {shot} zombies before being eaten: overwhelmed.'
        if not ammo:
            return f'You shot {shot} zombies before being eaten: ran out of ammo.'
        return zombie_shootout(zombies - 1, distance - 0.5, ammo - 1, shot + 1)
    
    return zombie_shootout(zombies, distance, ammo)


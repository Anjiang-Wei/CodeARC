def calculate_cog_rpms(cogs: list[int], n: int) -> list[float]:
    # Calculate RPM of the first cog
    first_cog_rpm = cogs[n] / cogs[0] * (-1 if n % 2 else 1)
    
    # Calculate RPM of the last cog
    last_cog_rpm = cogs[n] / cogs[-1] * (1 if (len(cogs) - n) % 2 else -1)
    
    # Return the RPMs as a list
    return [first_cog_rpm, last_cog_rpm]


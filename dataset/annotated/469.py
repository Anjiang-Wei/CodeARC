def convert_memory_size(memorysize: str) -> str:
    value, unit = memorysize.split(" ")
    
    kibis = ["KiB", "MiB", "GiB", "TiB"]
    kilos = ["kB", "MB", "GB", "TB"]
    
    if unit in kibis:
        # Convert from binary to decimal
        return str(round(float(value) * pow(1.024, kibis.index(unit) + 1), 3)) + " " + kilos[kibis.index(unit)]
    else:
        # Convert from decimal to binary
        return str(round(float(value) / pow(1.024, kilos.index(unit) + 1), 3)) + " " + kibis[kilos.index(unit)]


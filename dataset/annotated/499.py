def calculate_index_or_coordinates(
    x: int = None, 
    y: int = None, 
    n: int = None, 
    size: tuple[int, int] = None
) -> int | tuple[int, int] | None:
    if x is not None and y is not None and size is not None:
        # Calculate the 1D index from 2D coordinates
        return y * size[0] + x
    elif n is not None and size is not None:
        # Calculate the 2D coordinates from 1D index
        return (n % size[0], n // size[0])
    else:
        # Handle invalid input scenario
        return None


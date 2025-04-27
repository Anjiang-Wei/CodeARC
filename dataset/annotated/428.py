def create_hero_profile(name: str = 'Hero') -> dict:
    """
    :type name: str
    :rtype: dict
    """
    # Initialize hero attributes
    hero = {
        'name': name,
        'position': '00',
        'health': 100,
        'damage': 5,
        'experience': 0
    }
    
    return hero


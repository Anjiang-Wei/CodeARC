def analyze_tweet(tweet: str) -> str:
    import re
    from itertools import groupby

    CONFIG = {
        'FURY': " really",
        'FIRE': " and you",
        'FAKE': "Fake tweet.",
        'FURY_f': "I am{} furious.",
        'FIRE_f': "You{} are fired!"
    }

    # Check for invalid characters
    if re.findall(r'[^FURYIE]', tweet):
        return CONFIG['FAKE']
    
    lst = []
    # Group by occurrences of 'FURY' and 'FIRE'
    for k, g in groupby(re.findall(r'FURY|FIRE', tweet)):
        # Format the message based on the count of consecutive words
        lst.append(CONFIG[k + "_f"].format(CONFIG[k] * (len(list(g)) - 1)))
    
    # Join the messages or return 'Fake tweet.' if no valid words found
    return ' '.join(lst) or CONFIG['FAKE']


def is_codwars_url(url: str) -> bool:
    import re
    # Check if the URL matches the pattern for codwars.com domain
    return bool(re.match(r'^(https?://)?([a-z]+\.)*codwars\.com([/?].*)?$', url))


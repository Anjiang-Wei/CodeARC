def validate_phone_number(string: str) -> str:
    import re
    yes = "In with a chance"
    no = "Plenty more fish in the sea"
    
    # Remove dashes and check if the number matches the valid pattern
    cleaned_string = re.sub('-', '', string)
    if re.match(r'^(\+44|0)7[\d]{9}$', cleaned_string):
        return yes
    else:
        return no


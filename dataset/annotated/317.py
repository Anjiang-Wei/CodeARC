def get_favorite_drink(profession: str) -> str:
    d = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    # Convert input to lowercase and return the corresponding drink or "Beer" if not found
    return d.get(profession.lower(), "Beer")


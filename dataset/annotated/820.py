def calculate_permission_value(perm: dict) -> str:
    perms = {"r": 4, "w": 2, "x": 1}
    value = ""
    for permission in ["owner", "group", "other"]:
        # Calculate the sum of permission values for each category
        value += str(sum(perms.get(x, 0) for x in perm.get(permission, "---")))
    return value


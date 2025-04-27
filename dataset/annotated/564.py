def transform_string(s: str) -> str:
    return "".join(
        ("Iron " * c.isupper() + "Yard" * (c.lower() in "aeiou")).strip() or c for c in s
    )


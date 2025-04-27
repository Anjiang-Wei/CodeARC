def assess_sabbatical_eligibility(stg: str, value: int, happiness: int) -> str:
    sabbatical = (value + happiness + sum(1 for c in stg if c in "sabbatical")) > 22
    return "Sabbatical! Boom!" if sabbatical else "Back to your desk, boy."

